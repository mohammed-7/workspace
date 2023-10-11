# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, "app/index.html")


def departments(request):
    return render(request, "app/departments.html")


def services(request):
    return render(request, "app/services.html")
