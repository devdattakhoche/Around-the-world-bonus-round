from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Answer, Question
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import random
flag = 0
flag_count = 1
list_id = []
answer_count = 0

# Create your views here.

def Success(request):
    return render(request,'ATW/success.html')

def Wrong(request):
    return render(request,'ATW/Wrong_Ans.html')

def Home(request):
    print("Printed in Views.Home")
    global flag
    global flag_count
    global list_id
    global answer_count

    answer_count = 0
    # dictionary to be passed
    x = {}
    
    flag_count=1

    #faltu logic need to work on this
    question_no = random.randrange(1, 21)
    # for i in list_id:
    #     if(i == question_no):
    #         question_no = random.randrange(1, 7)
    # if question_no in list_id:
    #     question_no = random.randrange(1,2) not in list_id
    #     print(question_no)

    list_id.append(question_no)

    #till this part

    x['mytext'] = question_no
    x['flag'] = flag
    return render(request, 'ATW/Home.html', x)

@csrf_exempt
def Questions(request, Uid):
    print("Printed in Views.Questions")
    global flag
    global flag_count
    global list_id
    global answer_count

    if request.method == 'POST':
        Option = request.POST.get('Answer')
        Option = Option.strip()
        y = Answer.objects.get(Question_id=Uid)
        k = y.Ans 
        k = k.strip()
        print(Option,k)
        if(flag_count==6):
            flag_count = 1
            list_id.clear()
            dict1 = {'flag':flag,'question':'{}'.format('Sucess'),'flag_count':6,'answer_count':answer_count}
            return JsonResponse(dict1)
        if k.lower() == Option.lower():
            answer_count += 1
            flag = 0
            flag_count += 1

            if flag_count == 2:
                que_no=random.randrange(21,41) 
            if flag_count == 3:
                que_no=random.randrange(41,61)
            if flag_count == 4:
                que_no=random.randrange(61,81)
            if flag_count == 5:
                que_no=random.randrange(81,101)
            if flag_count == 6:
                que_no = 0
            
            question_no = str(que_no)
            list_id.append(question_no)
            dict1 = {'flag':flag,'question':'{}'.format(question_no),'flag_count':flag_count,'answer_count':answer_count}
            return JsonResponse(dict1)
            # return redirect('/Home/Question-'+question_no)
        else:
            flag = 1
            flag_count += 1
            if flag_count == 2:
                que_no=random.randrange(21,41) 
            if flag_count == 3:
                que_no=random.randrange(41,61)
            if flag_count == 4:
                que_no=random.randrange(61,81)
            if flag_count == 5:
                que_no=random.randrange(81,101)
            if flag_count == 6:
                que_no = 0
            
            question_no = str(que_no)
            # flag_count = 1
            # print(flag)
            list_id.clear()
            dict2 = {'flag':flag,'question':'{}'.format(question_no),'flag_count':flag_count,'answer_count':answer_count}
            print(dict2)
            return JsonResponse(dict2)
            # return render(request, 'ATW/Wrong_Ans.html')

    x = Question.objects.get(id=Uid)
    # print(x)
    params = {'pro': x, 'flag': flag, 'flag_count': flag_count}
    return render(request, 'ATW/questions.html', params)

def Timeout(request):
    return render(request, 'ATW/Timeout.html')