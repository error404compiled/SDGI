from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact


# Create your views here.
def index(request):
    context ={
        'variable1' : "hrithik sab ka bap h",
        'variable2' : "sanjay hrithik ka be baap h "
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is home page ")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page ")

def services(request):
    return render(request, 'servises.html')
    # return HttpResponse("this is services page ")

def contact (request):
    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        desc =request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()

    return render(request, 'contact.html')
    # return HttpResponse("this is contact page ")

def courses (request):
    return render(request, 'courses.html')

def stu_info (request):
    return render(request, 'stu_info.html')

def assingment (request):
    return render(request, 'assingment.html')

