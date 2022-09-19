from time import sleep
from .utils import csv_to_list, check_usernamekey_in_csv
from django.shortcuts import render, redirect, get_object_or_404
from .export_pdf import export_file
from .fetch import single_fetch_content
from .data_getter import populate_dict
from .evaluation import single_evaluation, do_group_evaluation
from .create_evaluation import new_evaluation, new_group_evaluation
from .models import Evaluation, GroupCSV, GroupEvaluation
from .tracker import raise_evaluation_clicks, raise_group_evaluation_clicks

from django.core.serializers import serialize

from django.http import HttpResponse
import json

def index(request):
    context = {}
    if request.method == "POST":
        eval = single_evaluation(
            populate_dict(single_fetch_content(request.POST["github_user"]))
        )
        new_eval = new_evaluation(eval)
        raise_evaluation_clicks()              
        print(type(request))
        return redirect("evaluation", uuid=new_eval.uuid)
    elif request.method == "GET" and 'github_user' in request.GET:        
        aval =  single_evaluation(
            populate_dict(single_fetch_content(request.GET["github_user"]))
        )
        data = json.dumps({'grade':aval['grade']})                 
        return HttpResponse(data, content_type="application/json")        
    return render(request, "index.html", context)


def group_index(request):
    context = {}

    if request.method == "POST":
        if request.FILES["file"]._name.endswith("csv"):
            csv_object = GroupCSV(file=request.FILES["file"])
            csv_object.save()
            csv_list = csv_to_list(csv_object.file.name)
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
