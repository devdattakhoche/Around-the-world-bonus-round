from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request,'ATW/Home.html')

def Questions(request):
    return render(request,'ATW/questions.html')