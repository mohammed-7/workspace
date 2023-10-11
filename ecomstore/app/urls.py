from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('departments/', views.departments),
    path('services/', views.services),


]
