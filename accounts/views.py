from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import (
    UsercreationForm
)

def signup(request):
    if request.method == 'POST':
        form = UsercreationForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request,'signup.html',{'form':form})
    form = UsercreationForm()
    return render(request,'signup.html',{'form':form})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user:
            login(request,user)
            return redirect('/')
        return render(request,'signin.html',{'error_message':'Your password or username is incorrect'})
    return render(request,'signin.html')

def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render(request,'signout.html')

def profile(request):
    return render(request,'profile.html',{'user':request.user})