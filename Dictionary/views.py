from django.shortcuts import render
from .models import UDict
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the dictionary index.")
