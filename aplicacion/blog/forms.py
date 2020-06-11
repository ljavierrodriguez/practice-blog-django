from django import forms
from .models import Category, Post, Comment


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'content')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'author', 'post')