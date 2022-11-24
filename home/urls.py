from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('General-Information', views.General_Information, name= 'General-Information'),
    path('services', views.services, name= 'services'),
    path('contact', views.contact, name= 'contact'),
    path('Committee', views.Committee, name= 'Committee'),
    path('Call-for-Papers', views.Call_for_Papers, name= 'Call-for-Papers'),
    path('Call-for-Reviews', views.Call_for_Reviews, name= 'Call-for-Reviews')
]