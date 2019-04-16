from django.urls import path

from . import views

app_name = 'UDictionary'
urlpatterns = [
    path('', views.index, name='index'),
    path('addword/', views.addword, name='addword'),
    path('<search_id>/', views.search, name='search')
]
