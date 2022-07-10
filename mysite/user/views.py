from json import load
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'user/home.html',{'username':""})



def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Hi {username} , your account created successfully')
            return redirect('user:home')
            #return render(request,'user/home.html',{'username':username})

    else:
        form=UserRegisterForm()

    
    return render(request,'user/register.html',{'form':form})

@login_required()
def profile(request):
    return render(request,"user/profile.html")