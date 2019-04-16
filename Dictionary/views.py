from django.shortcuts import render, redirect
from .models import Word, Desc
from django.contrib.auth.models import User
from django.http import HttpResponse

context = {
        'words': Word.objects.all(),
        'desc': Desc.objects.all()
    }


def index(request):
    context = {
        'words': Word.objects.all(),
        'desc': Desc.objects.all()
    }
    if request.method == 'POST':
        search_id = request.POST.get('title', None)
        try:
            word = Word.objects.filter(word_text__icontains=search_id)
            context['words'] = word
            print(word)
            if not word:
                word = Desc.objects.filter(desc_text__icontains=search_id)
                context['words'] = []
                for w in word:
                    context['words'].append(w.word)

        except Word.DoesNotExist:
            return HttpResponse("Word does not exist.")

    return render(request, 'Dictionary/home.html', context)


def addword(request):
    if request.method == 'POST':
        try:
            new_word = request.POST.get('new_word', None)
            word_desc = request.POST.get('word_desc', None)
            try:
                word = Word.objects.get(word_text=new_word)
            except Word.DoesNotExist:
                word = Word.objects.create(word_text=new_word)
            desc = Desc.objects.create(word=word, desc_text=word_desc, posted_by=User.objects.get(id=1))

            return redirect("UDictionary:index")
        except Word.DoesNotExist:
            return HttpResponse("Invalid Word Entry")
    return render(request, 'Dictionary/addword.html')

