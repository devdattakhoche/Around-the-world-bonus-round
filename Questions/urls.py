from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name = 'Home'),
    path('<int:id>',views.Questions,name = 'questions')
]