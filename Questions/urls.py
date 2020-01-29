from django.urls import path
from . import views

urlpatterns = [
    path('Home/', views.Home, name='Home'),
    path('Home/Question-<int:Uid>', views.Questions, name='Questions'),
    path('Home/Wrong', views.Wrong, name='Wrong'),
    path('Home/Question-Sucess', views.Success, name='Success'),
    path('Timeout', views.Timeout, name='Timeout'),
]
