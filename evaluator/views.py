from django.views.decorators.csrf import csrf_exempt
from .utils import csv_to_list, check_usernamekey_in_csv
from django.shortcuts import render, redirect, get_object_or_404
from .export_pdf import export_file
from .fetch import single_fetch_content
from .data_getter import populate_dict
from .serializer import serialize_eval
from .evaluation import single_evaluation, do_group_evaluation
from .create_evaluation import new_evaluation, new_group_evaluation
from .models import Evaluation, GroupCSV, GroupEvaluation
from .tracker import raise_evaluation_clicks, raise_group_evaluation_clicks
from django.http import HttpResponse, JsonResponse
from datetime import date, timedelta
from json import dumps
import requests


def index(request):
    context = {}
    if request.method == "POST":
        eval = single_evaluation(
            populate_dict(single_fetch_content(request.POST["github_user"]))
        )
        new_eval = new_evaluation(eval)
        raise_evaluation_clicks()
        return redirect("evaluation", uuid=new_eval.uuid)
    elif request.method == "GET" and "github_user" in request.GET:
        aval = (
            Evaluation.objects.all()
            .filter(github_user=request.GET["github_user"])
            .order_by("-evaluation_date")
        )
        if len(aval) > 0:
            aval = aval[0]
            data = dumps({"grade": aval.grade})
        else:
            aval = single_evaluation(
                populate_dict(single_fetch_content(request.GET["github_user"]))
            )
            data = dumps({"grade": aval["grade"]})
        return HttpResponse(data, content_type="application/json")
    return render(request, "index.html", context)


def group_index(request):
    context = {}

    if request.method == "POST":
        if request.FILES["file"]._name.endswith("csv"):
            csv_object = GroupCSV(file=request.FILES["file"])
            csv_object.save()
            csv_list = csv_to_list("media/" + csv_object.file.name)
            if not check_usernamekey_in_csv(csv_object, csv_list):
                request.session[
                    "erro"
                ] = 'Coluna "github_username" não existe dentro do arquivo csv!!!'
                return redirect("group-homepage")
            if "erro" in request.session:
                del request.session["erro"]
            csv_list = do_group_evaluation(csv_list)
            new_group_evaluation(csv_list, csv_object)
            raise_group_evaluation_clicks()
            return redirect("group-evaluation", uuid=csv_object.uuid)
        else:
            request.session["erro"] = "Arquivo com extensão inválida!!!"
            return redirect("group-homepage")

    return render(request, "group_index.html", context)


def evaluation(request, uuid: str):
    current_evaluation = get_object_or_404(Evaluation, uuid=uuid)
    context = {"evaluation": current_evaluation, "single": "single"}
    return render(request, "evaluation.html", context)


def group_evaluation(request, uuid: str):
    csv_object = get_object_or_404(GroupCSV, uuid=uuid)
    evaluations = GroupEvaluation.objects.all().filter(csv_file=csv_object)

    context = {"group_evaluation": evaluations, "group": "group"}
    return render(request, "group_evaluation.html", context)


def pdf_export(request, type: str, uuid: str):
    return export_file(type, uuid)


@csrf_exempt
def new_index(request):
    if request.method == "GET" and "github_user" in request.GET:
        refresh = False
        if "refresh" in request.GET:
            refresh = True if request.GET["refresh"].lower() == "true" else False
        user = request.GET["github_user"]
        eval = (
            Evaluation.objects.all()
            .filter(github_user=user)
            .order_by("-evaluation_date")
        )

        if len(eval) > 0:
            eval = eval[0]
            status = 200
            if date.today() - eval.evaluation_date > timedelta(days=3) or refresh:
                eval_dict = single_evaluation(populate_dict(single_fetch_content(user)))
                if not eval_dict["github"]:
                    return JsonResponse(
                        {"status": "false", "message": "precondition failed"},
                        status=412,
                    )
                eval = new_evaluation(eval_dict)
                status = 201
        else:
            eval_dict = single_evaluation(populate_dict(single_fetch_content(user)))
            if not eval_dict["github"]:
                return JsonResponse(
                    {"status": "false", "message": "precondition failed"}, status=412
                )
            eval = new_evaluation(eval_dict)
            status = 201

        return JsonResponse({"grade": eval.grade}, status=status)

    elif request.method == "POST":
        eval_dict = single_evaluation(
            populate_dict(single_fetch_content(request.POST["github_user"]))
        )

        if not eval_dict["github"]:
            return JsonResponse(
                {"status": "false", "message": "precondition failed"}, status=412
            )

        return JsonResponse(serialize_eval(new_evaluation(eval_dict)), status=201)

    else:
        return JsonResponse(
            {"status": "false", "message": "method not allowed"}, status=405
        )

def index_fastapi(request):
    context = {}
    if request.method == "POST":
        response = requests.get('https://b151-2804-2488-308b-7cf0-a028-d4be-c1ec-fbc8.sa.ngrok.io/evaluation/'+request.POST["github_user"])
        new_eval = new_evaluation(response.json())
        return redirect("evaluation", uuid=new_eval.uuid)
    return render(request, "index.html", context)


def group_index_fastapi(request):
    context = {}

    if request.method == "POST":
        if request.FILES["file"]._name.endswith("csv"):
            csv_object = GroupCSV(file=request.FILES["file"])
            csv_object.save()
            csv_list = csv_to_list("media/" + csv_object.file.name)
            request_string = '?'
            for user in csv_list:
                request_string+=f'user={user["github_username"]}&'
            if not check_usernamekey_in_csv(csv_object, csv_list):
                request.session[
                    "erro"
                ] = 'Coluna "github_username" não existe dentro do arquivo csv!!!'
                return redirect("group-homepage")
            if "erro" in request.session:
                del request.session["erro"]
            response = requests.get('https://b151-2804-2488-308b-7cf0-a028-d4be-c1ec-fbc8.sa.ngrok.io'+request_string)
            if response.status_code == 200:
                new_group_evaluation(response.json(), csv_object)
                return redirect("group-evaluation", uuid=csv_object.uuid)
            else:
                request.session[
                    "erro"
                ] = 'A requisição falhou!'
                return redirect("group-homepage")
        else:
            request.session["erro"] = "Arquivo com extensão inválida!!!"
            return redirect("group-homepage")

    return render(request, "group_index.html", context)