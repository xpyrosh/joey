from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Shiva',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 10, 2019'
    },
    {
        'author': 'Not Shiva',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 11, 2019'
    }
]


# home page view
def home(request):
    context = {
        'posts': posts,
    }

    return render(request, 'blog/home.html', context)


# about page view
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
