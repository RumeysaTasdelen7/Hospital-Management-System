from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Doctor


def  About(request):
    return render(request, 'about.html')

def Home(request):
    return render(request, 'home.html')

def Contact(request):
    return render(request, 'contact.html')


def Index(request):
    if not request.user.is_staff:
        return redirect ('login')
    return render(request, 'index.html')


def Login(reguest):
    error = ""
    if reguest.method == "POST":
        u = reguest.POST['uname']
        p = reguest.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(reguest, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(reguest, 'login.html', d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    
    logout(request)
    return redirect('login')


def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)