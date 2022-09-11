import uuid
import pyautogui
import csv
from PIL import Image
from .forms import CSVForm
from .utils import csv_to_list
from django.shortcuts import render, redirect, get_object_or_404
from evaluator.fetch import single_fetch_content
from evaluator.data_getter import populate_dict
from evaluator.evaluation import single_evaluation
from evaluator.create_evaluation import new_evaluation
from evaluator.models import Evaluation, GroupCSV
from evaluator.tracker import raise_evaluation_clicks


def index(request):
    context = {}
    if request.method == 'POST':
        print(request.POST['github_user'])
        eval = single_evaluation(populate_dict(single_fetch_content(request.POST['github_user'])))
        new_eval = new_evaluation(eval)
        raise_evaluation_clicks()
        return redirect('evaluation', uuid=new_eval.uuid)

    return render(request, 'index.html', context)

def group_index(request):
    context = {}
    return render(request, 'group_index.html', context)


def evaluation(request, uuid: str):
    current_evaluation = get_object_or_404(Evaluation, uuid=uuid)
    context = {'evaluation': current_evaluation}
    return render(request, 'evaluation.html', context)


def group_evaluation(request, uuid: str):
    csv_object = get_object_or_404(GroupCSV, uuid=uuid)
    csv_list = csv_to_list(csv_object.file.name)
    evaluation_list = []

    for person in csv_list:
        eval = single_evaluation(populate_dict(single_fetch_content(person['github_username'])))
        new_eval = new_evaluation(eval)
    raise_evaluation_clicks()

    context = {'group_evaluation': evaluation_list}
    return render(request, 'group_evaluation.html', context)


def create_csv_to_evaluation(request):
    if request.FILES['file']._name.endswith('csv'):
        csv_object = GroupCSV(
            file=request.FILES['file']
        )
        csv_object.save()
        print(dir(csv_object.file))
        csv_list = csv_to_list(csv_object.file.name)
        if 'github_username' not in csv_list[0]:
            csv_object.file.delete()
            csv_object.delete()
            request.session['erro'] = 'Chave "github_username" não existe no arquivo!!'
            return redirect('group-homepage')
        if 'erro' in request.session:
            del request.session['erro']
        return redirect('group-evaluation', uuid=csv_object.uuid)
    else:
        request.session['erro'] = 'Arquivo Inválido!!'
        return redirect('group-homepage')


def pdf_export(request):
    ...

