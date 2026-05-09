from django.urls import path, include

from accounts.views import register, edit_user_profile
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name = "register"),
    path('', include("django.contrib.auth.urls"), name = "accounts"),
    path('edit-profile/', edit_user_profile, name = "edit_user_profile"),
    path('toggle_theme/', views.toggle_theme, name = "toggle_theme")
]