from asyncio.windows_events import NULL
from typing import Text
from django.shortcuts import render



from django.http import HttpResponse


from django.shortcuts import get_object_or_404, render

from oj.models import  Question,user_score,submissions1,TestCases

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
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import subprocess
@login_required()
def problems(request):
    latest_question_list = Question.objects.all()
    #template = loader.get_template('oj/index.html')
    context = {
        'latest_question_list': latest_question_list,
        'prob': "true",
    }
    return render(request, 'oj/index.html', context)
   
    

@login_required()
def detail(request, problem_id):
    question = get_object_or_404(Question, pk=problem_id)
    form = SubmitedCode()
    return render(request, 'oj/detail.html', {'question': question,'form':form})

@login_required()
def SubmitProblem(request,problem_id):
    problem = get_object_or_404(Question,pk=problem_id)
    testcase=get_object_or_404(TestCases,question=problem_id)
    out=""
    code=""
    verd=""
    err=""
    s=""
    if request.method == 'POST':
        form = SubmitedCode(request.POST)
        if form.is_valid():
            code = form.cleaned_data['solution']
            
            f = open("solution.cpp", "w")
            f.write(code)
            f.close()

    
            data, temp = os.pipe()
  
            os.write(temp, bytes(testcase.input_testcases, "utf-8"));
            os.close(temp)
            compile_code='g++ solution.cpp -o solution.exe'
            run_code='solution.exe'
            try:
                c=subprocess.run(compile_code,shell = True,capture_output=True,text=True,check=True,timeout=5)
           
  
                try:
                    s=subprocess.run(run_code, stdin=data,capture_output=True, text=True,check=True, shell = True,timeout=0.1)
                except subprocess.TimeoutExpired:
                    out="Oops! TLE occurred."

            except subprocess.CalledProcessError as e:
                out="Compilation error"


          
            #out=s.decode("utf-8")
            if out=="":
                try:
                    out=s.stdout
                except:
                    out="Something went wrong"
            else:
                out=s

            
            if err=="" and out==testcase.otput_testcases:
                verd="AC"
            else:
                verd="WA"
            

              
    else:
        form = SubmitedCode()

    from datetime import datetime
    d=datetime.today().strftime('%Y-%m-%d')
    
    sub=submissions1(user_id=request.user,question=problem,Submission_verdict=verd,submission_date=d,submitted_code=code)
    sub.save()
    context = {
        'problem':problem,
        'output':out,
        'code':code,
        'verdict':verd,
        'error':err,
        'required_output':testcase.otput_testcases,
    }

    return render(request, 'oj/submit.html', context)
    

@login_required()
def latest_submissions(request):
    latest_sub=submissions1.objects.order_by('-submission_date')[:5]
    return render(request,'oj/latest_submission.html',{'latest_submissions':latest_sub})

@login_required()
def your_profile(request):
    #score=get_object_or_404(user_score,user_id=request.user)
    #sub=get_object_or_404(submissions1,user_id=request.user)
    return render(request,'user/profile.html',{'score':"f",'sub':"d"})