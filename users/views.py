from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm


def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("account")
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("account")
            else:
                messages.error(request, "Niepoprawne dane")
                return HttpResponse("Niepoprawne dane")


def register(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "users/register.html", {"form": form})


def account(request):
    if request.user.is_authenticated:
        return render(request, "users/profile.html", {"user": request.user})
    return redirect("login")


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect("login")
