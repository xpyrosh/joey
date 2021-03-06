from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import DictionaryListView, DictionaryCreateView

app_name = 'UDictionary'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', DictionaryListView.as_view(template_name='Dictionary/home.html'), name='index'),
    path('login/', LoginView.as_view(template_name='Dictionary/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Dictionary/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('addword/', views.addword, name='addword'),
    path('new/', DictionaryCreateView.as_view(template_name='Dictionary/new.html')),
    path('results/', views.search, name='search'),
    path('results/<str:search_id>/', views.results, name='results')
]
