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

def General_Information(request):
    return render(request, 'General Information.html')
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

def Committee (request):
    return render(request, 'Committee.html')

def Call_for_Papers (request):
    return render(request, 'Call-for-Papers.html')

def Call_for_Reviews (request):
    return render(request, 'Call-for-Reviews.html')

