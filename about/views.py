from django.shortcuts import render

def about(request):
    context = {
        'title': 'about'
    }
    return render(request,'about.html', context)

# Create your views here.
