from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(
            request.POST or None, request.FILES or None
        )  # Make sure both are included if needed
        if user_form.is_valid():
            user_form.save()
            return redirect("login")
    else:
        user_form = RegistrationForm()

    return render(request, "users/register.html", {"user_form": user_form})


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect("home")

    else:
        login_form = LoginForm()
    return render(request, "users/login.html", {"login_form": login_form})


@login_required
def user_profile(request):
    return render(request, "users/profile.html")


class CustomLogoutView(View):
    def get(self, request):
        return render(
            request, "users/logout.html"
        )  # Render the logout confirmation template

    def post(self, request):
        logout(request)  # Log the user out
        return redirect("home")  # Redirect to the home page
