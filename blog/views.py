from django.shortcuts import render

def blog(request):
    context = {
        'title' : 'blog'
    }
    return render(request, 'blog.html', context)

# Create your views here.
