from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from accounts.forms import UserProfileForm
# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.models import UserProfile

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
                   
@login_required
def toggle_theme(request):
    if request.method == "POST" and request.user.is_authenticated:
        request.user.profile.theme_preference = not request.user.profile.theme_preference
        request.user.profile.save()

        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return redirect("foodie_app:foodia_app_home")   

