from django.shortcuts import render
from .models import UDict
from django.http import HttpResponse


def index(request):
    context = {
        'test': UDict.objects.all()
    }
    return render(request, 'Dictionary/home.html', context)
    #return HttpResponse("Hello, world. You're at the dictionary index.")
