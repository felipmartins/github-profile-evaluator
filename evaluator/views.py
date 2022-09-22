from .utils import csv_to_list, check_usernamekey_in_csv
from django.shortcuts import render, redirect, get_object_or_404
from .export_pdf import export_file
from .fetch import single_fetch_content
from .data_getter import populate_dict
from .evaluation import single_evaluation, do_group_evaluation
from .create_evaluation import new_evaluation, new_group_evaluation
from .models import Evaluation, GroupCSV, GroupEvaluation
from .tracker import raise_evaluation_clicks, raise_group_evaluation_clicks
from django.http import HttpResponse, JsonResponse
from datetime import date, timedelta

from json import dumps


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
            request
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

def new_index(request):

    if request.method ==  "GET" and "github_user" in request.GET:
        user = request.GET["github_user"]
        eval = (
                Evaluation.objects.all()
                .filter(github_user=user)
                .order_by("-evaluation_date")
            )

        if len(eval) > 0:
                eval = eval[0]
                if date.today() - eval.evaluation_date > timedelta(days=3):
                    eval = new_evaluation(
                        single_evaluation(populate_dict(single_fetch_content(user)))
                    )
        else:
            eval = new_evaluation(
                single_evaluation(populate_dict(single_fetch_content(user)))
            )
        
        return JsonResponse({'grade': eval.grade})
    
    if request.method ==  "GET" and "github_user" in request.GET and "refresh" in request.GET:
        if request.query_params["refresh"].lower() == 'true':
            eval = new_evaluation(single_evaluation(populate_dict(single_fetch_content(request.GET["github_user"]))))
            return JsonResponse({'grade': eval.grade})
        else:
            user = request.GET["github_user"]
            eval = (
                    Evaluation.objects.all()
                    .filter(github_user=user)
                    .order_by("-evaluation_date")
                )

            if len(eval) > 0:
                    eval = eval[0]
                    if date.today() - eval.evaluation_date > timedelta(days=3):
                        eval = new_evaluation(
                            single_evaluation(populate_dict(single_fetch_content(user)))
                        )
            else:
                eval = new_evaluation(
                    single_evaluation(populate_dict(single_fetch_content(user)))
                )
            
            return JsonResponse({'grade': eval.grade})
                
    elif request.method ==  "POST":
        ...
    else:
        return JsonResponse({'error':'not found'})
