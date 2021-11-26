from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "pHome" ),
    path('blogpost/<int:id>/', views.blogpost, name = "blogPost" ),]