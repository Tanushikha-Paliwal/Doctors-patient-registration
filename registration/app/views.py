from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password , check_password
from . models import *
from django.http.response import HttpResponse
# Create your views here.

def loginview(request):
    return render(request, 'login.html')

def index(request):
    return render(request , 'index.html')

def about(request):
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html')

def departments(request):
    return render(request , 'departments.html')

def doctors(request):
    return render(request , 'doctors.html')


def registration(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        password = make_password(request.POST['password'])
        if Patient.objects.filter(email=email).exists():
            return HttpResponse("Patient already registered")
        else:
            Patient.objects.create(name=name , phone=phone , email=email , password=password , message=message)
            return redirect("/loginview/")
        
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if Patient.objects.filter(email=email).exists():
            obj = Patient.objects.get(email=email)
            pwd = obj.password
            if check_password(password,pwd):
                return redirect('/departments/')
            else:
                return HttpResponse("Incorrect password")
        else:
            return HttpResponse("Email is not registered")



