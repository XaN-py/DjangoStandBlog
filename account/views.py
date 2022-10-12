from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def userlogin(request):
    if request.user.is_authenticated:
        return redirect("home_app:index")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home_app:index")
        else:
            redirect("account:login")
    return render(request, 'account/login.html', {})


def user_register(request):
    context = {"errors": []}

    if request.user.is_authenticated:
        print("2")
        return redirect("home_app:index")

    if request.method == "POST":
        U_username = request.POST.get("username")
        U_email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if User.objects.get(email=U_email):
            context["errors"].append('email is register')
            return render(request, 'account/register.html', context)

        if pass1 != pass2:
            context["errors"].append('Password 1 and 2 not mach')

            return render(request, 'account/register.html', context)
        else:
            user = User.objects.create(username=U_username, password=pass1, email=U_email)
            login(request, user)
            return redirect("account:login")

    return render(request, 'account/register.html', {})


def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("home_app:index")
    else:
        return redirect("home_app:index")
