from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Answer, Question
import random
flag = 0
flag_count = 1
list_id = []

# Create your views here.

def Home(request):
    print("Printed in Views.Home")
    global flag
    global flag_count
    global list_id

    # dictionary to be passed
    x = {}
    
    flag_count=1

    #faltu logic need to work on this
    question_no = random.randrange(1, 7)
    for i in list_id:
        if(i == question_no):
            question_no = random.randrange(1, 7)

    list_id.append(question_no)

    #till this part

    x['mytext'] = question_no
    x['flag'] = flag
    return render(request, 'ATW/Home.html', x)


def Questions(request, Uid):
    print("Printed in Views.Questions")
    global flag
    global flag_count
    global list_id
    # print(Uid)
    if request.method == 'POST':
        Option = request.POST.get('Answer')
        print(Option)
        y = Answer.objects.get(Question_id=Uid)
        if y.Ans == Option:
            flag = 0
            flag_count += 1

            if(flag_count == 6):
                flag_count = 1
                list_id.clear()
                return render(request, 'ATW/success.html')
    
            question_no = str(random.randrange(1, 7))
            return redirect('/Home/Question-'+question_no)
        else:
            flag = 1
            flag_count = 1
            # print(flag)
            list_id.clear()
            return render(request, 'ATW/Wrong_Ans.html')

    x = Question.objects.get(id=Uid)
    # print(x)
    params = {'pro': x, 'flag': flag, 'flag_count': flag_count}
    return render(request, 'ATW/questions.html', params)

def Timeout(request):
    return render(request, 'ATW/Timeout.html')