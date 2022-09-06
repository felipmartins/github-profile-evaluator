from django.shortcuts import render
from evaluator.fetch import single_fetch_content
from evaluator.data_getter import populate_dict
from evaluator.evaluation import single_evaluation
from evaluator.create_evaluation import new_evaluation
from evaluator.tracker import raise_evaluation_clicks

def index(request):
    context = { 'table': False

    }

    if request.method == 'POST':
        print(request.POST['github_user'])

        eval = single_evaluation(populate_dict(single_fetch_content(request.POST['github_user'])))
        new_evaluation(eval)
        raise_evaluation_clicks()

        context = {

            'git_user': eval,
            'table': True
            
        }
    


    return render(request, 'index.html', context)
