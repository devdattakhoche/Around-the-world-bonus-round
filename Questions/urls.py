from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name = 'Home'),
    path('questions/1',views.Questions,name = 'questions')
]