from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('departments/',views.departments),
    path('doctors/',views.doctorsview),
    path('patient/',views.patient),
    path('patientregistrationview/',views.patient_registration_view),
    path('patientregistration/',views.patient_registration),
    path('registration/',views.doctors_registration),
    path("doctorlogin/",views.doctors_login),
    path("login/",views.login),
    path('contactus/',views.contact_us),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
