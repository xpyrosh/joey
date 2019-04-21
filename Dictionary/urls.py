from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'UDictionary'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='Dictionary/login.html')),
    path('addword/', views.addword, name='addword'),
    path('results/', views.search, name='search'),
    path('results/<str:search_id>/', views.results, name='results')
]
