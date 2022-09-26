"""user controller"""
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def logout_user(request):
    """destroy session for requested request"""
    logout(request)
    return HttpResponseRedirect(reverse("base:index"))


def login_user(request):
    """logs a user in into the session"""

    # when method is post
    if request.method == "POST":

        # get username and password
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        # check for username and password
        if not (username and password):
            messages.error(request, "Please provide your username.")
            messages.error(request, "Please provide your password.")
        elif not username:
            messages.error(request, "Please provide your username.")
        elif not password:
            messages.error(request, "Please provide your password.")
        else:
            # try to authenticate user
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                if not request.POST.get("remember_me"):
                    request.session.set_expirey(0)
                return HttpResponseRedirect(reverse("base:index"))
            messages.error(request, "Invalid username and/or password.")
    # when method is not post
    context = {"title": "login"}
    return render(request, "user/authenticate.html", context)


def register_user(request):
    """register and login a new user"""
    pass
