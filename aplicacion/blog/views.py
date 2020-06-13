from django.shortcuts import render, redirect
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
        form = forms.PostForm(request.POST)
        post = form.save(commit=False)
        post.author = request.user
        post.save() 
        if post:
            return redirect("blog")
        else:
            return render(request, template_name='blog/create.html', context={"form": form})
    form = forms.PostForm()
    return render(request, template_name='blog/create.html', context={"form": form})


def edit_post(request, id):
    post = models.Post.objects.get(id=id)
    if request.method == 'POST':
        form = forms.PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog")
        else:
            return render(request, template_name='blog/edit.html', context={"form": form})
    
    form = forms.PostForm(instance=post)
    return render(request, template_name='blog/edit.html', context={"form": form, "id": id})


def delete_post(request, id):
    post = models.Post.objects.get(id=id)
    post.delete()
    return redirect("blog")