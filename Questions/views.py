from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Answer,Question
import random

# Create your views here.
def Home(request):
    print("Printed in Views.Home")
    question_no = random.randrange(1,7)
    # dictionary to be passed
    x = {}
    x['mytext'] = question_no
 
    return render(request,'ATW/Home.html',x)

def Questions(request,Uid):
    print("Printed in Views.Questions")
    print(Uid)
    if request.method == 'POST':
        Option = request.POST.get('Answer')
        print(Option)
        y = Answer.objects.get(Question_id = Uid)
        if y.Ans == Option:
            question_no = str(random.randrange(1,7))
            return redirect('/Home/Question-'+question_no)
        else:
            return render(request,'ATW/Wrong_Ans.html')

    x = Question.objects.get(id = Uid) 
    print(x)
    params = { 'pro': x }

    return render(request,'ATW/questions.html',params)