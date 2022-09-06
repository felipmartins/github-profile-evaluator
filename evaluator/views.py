from django.shortcuts import render
from evaluator.fetch import single_fetch_content
from evaluator.data_getter import populate_dict
from time import sleep

def index(request):
    context = { 

    }

    if request.method == 'POST':
        print(request.POST['github_user'])

        context = {

            'git_user': populate_dict(single_fetch_content(request.POST['github_user']))
            
        }
    


    return render(request, 'index.html', context)
