import email
from multiprocessing import context
from weakref import ref
from django.shortcuts import render, HttpResponse
from flask import request
from datetime import date, datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable1":"this is great",
        "variable2":"awadhesh is also great"
    }
    return render(request, 'index.html',context)
   # return HttpResponse("this is home page")

def about(request):
    # return HttpResponse("this is about page")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("this is services page")
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    # return HttpResponse("this is contact page")
    return render(request, 'contact.html')