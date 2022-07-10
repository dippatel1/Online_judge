from django.shortcuts import render



from django.http import HttpResponse


from django.shortcuts import get_object_or_404, render

from oj.models import  Question,user_score,Submissions,TestCases

import os
from .forms import SubmitedCode




#=======================================================
from json import load
from multiprocessing import context
from re import template
from unittest import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .forms import SubmitedCode


#----------------------------------------------------

#--------------------------------------------
import sys
from io import StringIO
import contextlib

#-----------------------------------------
from django.contrib.auth.decorators import login_required
@login_required()
def problems(request):
    latest_question_list = Question.objects.all()
    #template = loader.get_template('oj/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'oj/index.html', context)
   
    

@login_required()
def detail(request, problem_id):
    question = get_object_or_404(Question, pk=problem_id)
    form = SubmitedCode()
    return render(request, 'oj/detail.html', {'question': question,'form':form})

@login_required()
def SubmitProblem(request,problem_id):
    # f=request.FILES['solution1']
    # with open("C:/Users/91832/Desktop/Oj/mysite/dip/solution.cpp",'wb+') as dest:
    #     for chunk in f.chunks():
    #         dest.write(chunk)
    # os.system('g++ /C:/Users/91832/Desktop/Oj/mysite/dip/solution.cpp')
    # os.system('./a.out < C:/Users/91832/Desktop/Oj/mysite/dip/input.txt > C:/Users/91832/Desktop/Oj/mysite/dip/output.txt')
    

    problem = get_object_or_404(Question,pk=problem_id)
    output=""
    code=""
    if request.method == 'POST':
        form = SubmitedCode(request.POST)
        if form.is_valid():
            code = form.cleaned_data['solution']
            # if(compiler(code)):
            #     print("accepted")
            # else:
            #     print("Wrong Answer")
            #codeObj=compile(code,problem.question_name+".py",'exec')
            f = open("./dip/solution.cpp", "w")
            f.write(code)
            f.close()

            os.system('g++ ./dip/solution.cpp')
            os.system('a < ./dip/input.txt > ./dip/output.txt')

            f = open("./dip/output.txt","r")
            output=(f.read())


              
    else:
        form = SubmitedCode()
    
    context = {
        'problem':problem,
        'output':output,
        'form':form,
        'code':code
    }

    return render(request, 'oj/submit.html', context)
    
