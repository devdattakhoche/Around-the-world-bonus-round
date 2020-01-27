from django.urls import path
from . import views

urlpatterns = [
    path('Home/', views.Home, name='Home'),
    path('Home/Question-<int:Uid>', views.Questions, name='Questions'),
    path('Timeout', views.Timeout, name='Timeout'),
]
