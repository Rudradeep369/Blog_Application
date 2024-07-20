from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Profile


# Create your views here.


def home(request):
    return render(request,'home.html')

def profile(request):
    if request.user.is_authenticated:
        profiles=Profile.objects.exclude(user=request.user)
        return render(request,'profile.html',{"profiles":profiles})
    else:
        messages.success(request,("You must be logged in to view Profile..."))
        return redirect("home")