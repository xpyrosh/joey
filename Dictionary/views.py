from django.shortcuts import render
from .models import Word, Desc
from django.http import HttpResponse


def index(request):
    context = {
        'words': Word.objects.all(),
        'desc': Desc.objects.all()
    }
    if request.method == 'POST':
        search_id = request.POST.get('title', None)
        try:
            word = Word.objects.get(word_text=search_id)
            context['words'] = [word]
            print(context['words'])
        except Word.DoesNotExist:
            return HttpResponse("Word does not exist.")

    return render(request, 'Dictionary/home.html', context)


    # def search(request):
    #     if request.method == 'POST':
    #         search_id = request.POST.get('textfield', None)
    #         try:
    #             word = Word.objects.get(word_text = search_id)
    #             html = ("<h1>%s<h1/>", word)
    #             return HttpResponse(html)
    #         except Word.DoesNotExist:
    #             return HttpResponse("Word does not exist.")
    #     else:
    #         return render(request, 'Dictionary/search.html')
