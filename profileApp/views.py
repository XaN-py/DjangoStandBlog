from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from .models import Profile


# Create your views here.

def user_profile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.all()

        return render(request, "profileApp/profile.html", {'profile': profile})
    else:
        return redirect("account:login")