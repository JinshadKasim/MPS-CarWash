from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'customer/index.html')

def login(request):
    return render(request,'customer/login.html')

def contact(request):
    return render(request,'customer/contact.html')
    