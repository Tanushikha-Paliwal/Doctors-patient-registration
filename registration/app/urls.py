from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('departments/',views.departments),
    path('doctors/',views.doctors),
    path('registration/',views.registration),
    path("login/",views.login),
    path("loginview/",views.loginview),
]
