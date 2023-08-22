from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.http.response import HttpResponse

# Create your views here.


def login(request):
    return render(request, "login.html")


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def departments(request):
    return render(request, "departments.html")


def patient(request):
    return render(request , "patient.html")


def doctorsview(request):
    doctors = Doctors.objects.all()
    return render(request, "doctors.html", {"doctors": doctors})


def patient_registration_view(request):
    patient = Patient.objects.all()
    add_doctor = Doctors.objects.all()
    redirect("/patientregistrationview/")
    return render(request, "patientregistration.html" , {"patient":patient , "add_doctor":add_doctor})


def patient_registration(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("mobile")
        email = request.POST.get("email")
        report = request.POST.get("report")
        gender = request.POST.get("gender")
        doctor_add = request.POST.get("doctor")
        doctor = Doctors.objects.get(id=doctor_add)
        password = make_password(request.POST.get("password"))
        if Patient.objects.filter(email=email).exists():
            return HttpResponse("Patient already registered")
        elif Patient.objects.filter(phone=phone).exists():
            return HttpResponse("mobile number already exists")
        else:
            Patient.objects.create(
                name=name,
                phone=phone,
                email=email,
                password=password,
                report=report,
                gender=gender,
                doctor=doctor,
            )
            return HttpResponse("Patient registered successfully")
            patient = Patient.objects.all()
            add_doctor = Doctors.objects.all()
            return redirect(request, "doctors.html" , {"patient":patient , "add_doctor":add_doctor})
    else:
        patient = Patient.objects.all()
        add_doctor = Doctors.objects.all()
        return render(request, "patientregistration.html" , {"patient":patient , "add_doctor":add_doctor})



def doctors_registration(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("mobile")
        email = request.POST.get("email")
        password = make_password(request.POST.get("password"))
        degree = request.POST.get("degree")
        specialization = request.POST.get("specialization")
        if Doctors.objects.filter(email=email).exists():
            return HttpResponse("Doctor already registered")
        else:
            Doctors.objects.create(
                name=name,
                phone=phone,
                email=email,
                password=password,
                degree=degree,
                specialization=specialization,
            )
            return redirect("/login/")


def doctors_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        if Doctors.objects.filter(email=email).exists():
            obj = Doctors.objects.get(email=email)
            pwd = obj.password
            if check_password(password, pwd):
                return redirect("/patient/")
            else:
                return HttpResponse("Incorrect password")
        else:
            return HttpResponse("Email is not registered")


