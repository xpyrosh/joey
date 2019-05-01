from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from .models import Word, Desc
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView, CreateView
from django.forms import modelform_factory, inlineformset_factory
from django.db import transaction

context = {
        'words': Word.objects.all(),
        'desc': Desc.objects.all()
    }


def index(request):
    context = {
        'words': Word.objects.all(),
        'desc': Desc.objects.all()
    }

    return render(request, 'Dictionary/home.html', context)


class DictionaryListView(ListView):
    model = Word
    context_object_name = 'words'


class DictionaryCreateView(CreateView):
    model = Word
    fields = ['word_text']
    success_url = reverse_lazy('UDictionary:index')

    def get_context_data(self, **kwargs):
        context_data = super(DictionaryCreateView, self).get_context_data(**kwargs)
        desc_form = modelform_factory(model=Desc, fields=['desc_text'])

        if self.request.method == 'POST':
            form_data = self.request.POST
            desc_form = desc_form(data=form_data)

        context_data['desc_form'] = desc_form
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        desc_form = context_data.get('desc_form')

        if desc_form.is_valid():
            with transaction.atomic():
                word_instance = form.save() # save Word
                desc_instance = desc_form.save(commit=False)
                desc_instance.posted_by = self.request.user
                desc_instance.word = word_instance
                desc_instance.save()
                return super(DictionaryCreateView, self).form_valid(form)

        self.render_to_response(context_data)




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
    # Defining the posted_by field if logged
    if request.user.is_authenticated:
        current_user = request.user.id
    else:
        current_user = 1

    if request.method == 'POST':
        try:
            new_word = request.POST.get('new_word', None)
            word_desc = request.POST.get('word_desc', None)
            try:
                word = Word.objects.get(word_text=new_word)
            except Word.DoesNotExist:
                word = Word.objects.create(word_text=new_word)
            desc = Desc.objects.create(word=word, desc_text=word_desc, posted_by=User.objects.get(id=current_user))

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

