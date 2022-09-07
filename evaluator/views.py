import pyautogui
from PIL import Image
from django.shortcuts import render, redirect, get_object_or_404
from evaluator.fetch import single_fetch_content
from evaluator.data_getter import populate_dict
from evaluator.evaluation import single_evaluation
from evaluator.create_evaluation import new_evaluation
from evaluator.models import Evaluation
from evaluator.tracker import raise_evaluation_clicks


def index(request):
    context = {}
    if request.method == 'POST':
        print(request.POST['github_user'])
        eval = single_evaluation(populate_dict(single_fetch_content(request.POST['github_user'])))
        new_eval = new_evaluation(eval)
        raise_evaluation_clicks()
        return redirect('evaluation', id=new_eval.id)
    
    return render(request, 'index.html', context)


def evaluation(request, id: int):
    current_evaluation = get_object_or_404(Evaluation, id=id)
    context = {'evaluation': current_evaluation}
    return render(request, 'evaluation.html', context)

def pdf_export(request):
 
    ...
