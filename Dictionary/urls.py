from django.urls import path

from . import views

app_name = 'UDictionary'
urlpatterns = [
    path('', views.index, name='index'),
    path('addword/', views.addword, name='addword'),
    path('results/', views.search, name='search'),
    path('results/<str:search_id>/', views.results, name='results')
]
