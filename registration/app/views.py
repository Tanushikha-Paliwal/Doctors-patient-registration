from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.http.response import HttpResponse
from django.contrib import messages


# Create your views here.


def login(request):
    return render(request, "login.html")


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    contact = Contact.objects.all()
    return render(request, "contact.html" , {"contact":contact})


def departments(request):
    return render(request, "departments.html")


def patient(request):
    patient = Patient.objects.all()
    return render(request, "patient.html",{"patient":patient})


def doctorsview(request):
    doctors = Doctors.objects.all()
    return render(request, "doctors.html", {"doctors": doctors})


def patient_registration_view(request):
    patient = Patient.objects.all()
    add_doctor = Doctors.objects.all()
    # redirect("/patientregistrationview/")
    return render(
        request,
        "patientregistration.html",
        {"patient":patient ,"add_doctor": add_doctor},
    )


def patient_registration(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("mobile")
        email = request.POST.get("email")
        reports = request.FILES.get("report")
        gender = request.POST.get("gender")
        doctor__add_doctor = request.POST["doctor"]
        # print(doctor__add_doctor)
        # print("____________________aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa__________________")

        doctor_obj = Doctors.objects.get(id=doctor__add_doctor)
        # print(doctor_obj)
        # print("____________________hear__________________")
        if Patient.objects.filter(email=email).exists():
            messages.error(request ,"Patient already registered")
        elif Patient.objects.filter(phone=phone).exists():
            messages.error(request ,"mobile number already exists")
        else:
            Patient.objects.create(
                name=name,
                phone=phone,
                email=email,
                reports=reports,
                gender=gender,
                doctor=doctor_obj,
            )
            patient= Patient.objects.all()
            add_doctor = Doctors.objects.all()
            # print(add_doctor)
            return render(request, "patient.html", {"patient":patient,"add_doctor": add_doctor})
    else:
        patient = Patient.objects.all()
        add_doctor = Doctors.objects.all()
        return render(
            request,
            "patientregistration.html",
            {"patient": patient, "add_doctor": add_doctor},
        )


def doctors_registration(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("mobile")
        email = request.POST.get("email")
        password = make_password(request.POST.get("password"))
        degree = request.POST.get("degree")
        specialization = request.POST.get("specialization")
        if Doctors.objects.filter(email=email).exists():
            messages.error(request ,"Doctor already registered")
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
                messages.error(request ,"Incorrect password")
        else:
            messages.error(request ,"Email is not registered")


def contact_us(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        if Contact.objects.filter(email=email).exists():
            messages.error(request , "Email Already Exists......")
        elif Contact.objects.filter(phone=phone).exists():
            messages.error(request , "Phone number already exists..")
        else:
            Contact.objects.create(
                name=name,
                phone=phone,
                email=email,
                message =message
            )
            messages.success(request,"u will be informed soon....")
            details = Contact.objects.all()
            return render(request , "contact.html" , {"details":details})
            