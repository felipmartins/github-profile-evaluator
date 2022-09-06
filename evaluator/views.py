from django.shortcuts import render

def index(request):
    context = { 

    }

    if request.method == 'POST':
        print(request.POST['github_user'])

        context = {
            
        }
    


    return render(request, 'index.html', context)
