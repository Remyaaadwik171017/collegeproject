
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def registration(request):
    return render(request,"Registration.html")
def login(request):
    return render(request,"login.html")
def homepage(request):
    return render(request,"home.html")
def leaveapplication(request):
    return HttpResponse('<h1> Apply for leave</h1>')
def viewtimetable(request):
    return HttpResponse('<h1> Timetable</h1>')
def postfeedback(request):
    return render(request,"feedback.html")
def logout(request):
    return render(request,"home.html")
def getreg(request):
    first_name=request.POST.get("fname")
    last_name=request.POST.get("lname")
    email=request.POST.get("email")
    user_name=request.POST.get("uname")
    password=request.POST.get("pwd")
    print(first_name,last_name,email,user_name,password)
    return render(request,"home.html")
def getlogin(request):
    user_name=request.POST.get("uname")
    password=request.POST.get("pwd")
    print(user_name,password)
    return render(request,"home.html")