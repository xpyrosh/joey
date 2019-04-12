from django.shortcuts import render
from .models import Word, Desc
from django.http import HttpResponse


def index(request):
    context = {
        'words': Word.objects.all(),
        'desc': Desc.objects.all()
    }
    return render(request, 'Dictionary/home.html', context)

