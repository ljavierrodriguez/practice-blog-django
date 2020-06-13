from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blog/", views.blog, name="blog"),
    path("blog/create", views.create_post, name="posts.create"),
    path("blog/<int:id>/edit", views.edit_post, name="posts.edit"),
    path("blog/<int:id>/delete", views.delete_post, name="posts.delete"),
]
