from django.shortcuts import render,redirect
from django.http import HttpResponse
from user_app.forms import CustomRegistrationForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method=='POST':
        form_register = CustomRegistrationForm(request.POST)
        if form_register.is_valid():
            form_register.save()
            messages.success(request,"Account registration completed.Please Login Now!")
            return redirect('register')
    else:
        form_register = CustomRegistrationForm()
    return render(request,'register.html',{'form_register':form_register})