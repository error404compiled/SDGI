from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('about', views.about, name= 'about'),
    path('services', views.services, name= 'services'),
    path('contact', views.contact, name= 'contact'),
    path('courses', views.courses, name= 'courses'),
    path('stu_info', views.stu_info, name= 'stu_info'),
    path('assingment', views.assingment, name= 'assingment')
]