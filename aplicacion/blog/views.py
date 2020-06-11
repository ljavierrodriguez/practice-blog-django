from django.shortcuts import render
from . import models
from . import forms

# Create your views here.
def home(request):
    return render(request, template_name='blog/home.html', context={})

def blog(request):
    posts = models.Post.objects.all()
    return render(request, template_name='blog/listado.html', context={"posts": posts})


def create_post(request):
    if request.method == 'POST':
        pass
    
    form = forms.PostForm(instance=models.Post)
    return render(request, template_name='blog/create.html', context={"form": form})