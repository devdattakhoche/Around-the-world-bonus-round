from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def Home(request):
    question_no = random.randrange(1,81)
    # dictionary to be passed
    x = {}
    x['mytext'] = question_no
 
    return render(request,'ATW/Home.html',x)

def Questions(request,id):
    print(id)
    return render(request,'ATW/questions.html')