from time import sleep
from .utils import csv_to_list
from django.shortcuts import render, redirect, get_object_or_404
from evaluator.fetch import single_fetch_content
from evaluator.data_getter import populate_dict
from evaluator.evaluation import single_evaluation, do_group_evaluation
from evaluator.create_evaluation import new_evaluation, new_group_evaluation
from evaluator.models import Evaluation, GroupCSV, GroupEvaluation
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

    if request.method == "POST":
        if request.FILES['file']._name.endswith('csv'):
            csv_object = GroupCSV(
                file=request.FILES['file']
            )
            csv_object.save()
            csv_list = csv_to_list(csv_object.file.name)
            if 'github_username' not in csv_list[0]:
                csv_object.file.delete()
                csv_object.delete()
                request.session['erro'] = 'Chave "github_username" não existe no arquivo!!'
                return redirect('group-homepage')
            if 'erro' in request.session:
                del request.session['erro']
            csv_list = do_group_evaluation(csv_list)
            new_group_evaluation(csv_list, csv_object)
            raise_evaluation_clicks
            sleep(1)
            return redirect('group-evaluation', uuid=csv_object.uuid)
        else:
            request.session['erro'] = 'Arquivo Inválido!!'
            return redirect('group-homepage')

    return render(request, 'group_index.html', context)


def evaluation(request, uuid: str):
    current_evaluation = get_object_or_404(Evaluation, uuid=uuid)
    context = {'evaluation': current_evaluation}
    return render(request, 'evaluation.html', context)


def group_evaluation(request, uuid: str):
    csv_object = get_object_or_404(GroupCSV, uuid=uuid)
    evaluations = GroupEvaluation.objects.all().filter(csv_file=csv_object)

    context = {'group_evaluation': evaluations}
    return render(request, 'group_evaluation.html', context)


def pdf_export(request):
    ...

