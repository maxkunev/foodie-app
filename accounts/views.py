from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from accounts.forms import UserProfileForm
# Create your views here.
from django.contrib import messages

def register(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            messages.success(request, "The user has been registered!")
            return redirect("foodie_app:foodie_app_home")
    context = {
        "form": form
    }
    return render(request, "registration/register.html", context)

def edit_user_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "The profile has been edited!")
            return redirect("accounts:edit_user_profile")
    else:
        form = UserProfileForm(instance = request.user.profile)
        
    return render(request, "registration/edit_profile.html", context={"form": form})
                   

        
        