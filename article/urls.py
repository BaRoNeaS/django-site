from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"
urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('addarticle/',views.addarticle,name = "addarticle"),
    path('article/<str:title>',views.detail,name = "detail"),
    path('update/<str:title>',views.updateArticle,name = "update"),
    path('delete/<str:title>',views.deleteArticle,name = "delete"),
    path('/blog',views.blog,name = "blog"),
    path('/comment/<str:title>',views.addComment,name = "comment"),
]
