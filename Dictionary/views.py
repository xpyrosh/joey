from django.shortcuts import render, redirect, reverse
from .models import Word, Desc
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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
        context['search_id'] = search_id
        try:
            word = Word.objects.filter(word_text__icontains=search_id)
            context['words'] = word
            if not word:
                word = Desc.objects.filter(desc_text__icontains=search_id)
                context['words'] = []
                for w in word:
                    context['words'].append(w.word)

        except Word.DoesNotExist:
            return HttpResponse("Word does not exist.")

    return render(request, 'Dictionary/home.html', context)


def search(request):
    return redirect(reverse('UDictionary:results', kwargs={'search_id': request.POST.get('search_id')}))


def results(request, search_id):
    context['search_id'] = search_id
    try:
        word = Word.objects.filter(word_text__icontains=search_id)
        context['words'] = word
        if not word:
            word = Desc.objects.filter(desc_text__icontains=search_id)
            context['words'] = []
            for w in word:
                context['words'].append(w.word)

    except Word.DoesNotExist:
        return HttpResponse("Word does not exist.")
    return render(request, 'Dictionary/search.html', context)


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


def login(request):
    return render(request, 'Dictionary/login.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            form.save()
            return redirect('UDictionary:login')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'Dictionary/register.html', context)

