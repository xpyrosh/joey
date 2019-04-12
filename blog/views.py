from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

# home page view


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


# about page view
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
