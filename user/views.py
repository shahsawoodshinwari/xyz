"""user controller"""
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


from .models import Profile
from .forms import LoginForm

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
        remember_me = request.POST.get("remember_me")
        form = LoginForm(username, password)
        # check for username and password
        if not form.is_valid():
            print("not valid")
        # if not username:
        #     messages.error(request, "Please provide your username.")
        # elif not password:
        #     messages.error(request, "Please provide your password.")
        else:
            # try to authenticate user
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                return HttpResponseRedirect(reverse("base:index"))
            messages.error(request, "Invalid username and/or password.")
    # when method is not post
    context = {"title": "login"}
    return render(request, "user/login.html", context)


def register_user(request):
    """register and login a new user"""
    # when method is post
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        confirmation = request.POST.get("confirmation")
        if not username:
            messages.error(request, "Please provide your username.")
        elif not password:
            messages.error(request, "Please provide your password.")
        elif not confirmation or confirmation != password:
            messages.error(request, "Please confirm your passowrd.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        else:
            user = User.objects.create(
                username=username, email=username, password=password
            )
            login(request, user)
            messages.success(request, "Registered and logged in successfully.")
            return HttpResponseRedirect(reverse("base:index"))
    context = {"title": "register"}
    return render(request, "user/register.html", context)


def profile(request):
    """manages the profile of user"""
    if request.method == "POST":
        profile = Profile(
            user=request.user, picture=request.FILES.get("profile_picture")
        )
        profile.save()

    context = {"title": "profile"}
    return render(request, "user/profile.html", context)


class Password(object):
    def __init__(self, arg):
        self.arg = arg

    def is_numeric(self):
        return self.arg.isdigit()

    def is_strong(self):
        return any(char in "!@#$%^&*" for char in self.arg)

    def has_valid_length(self):
        return len(self.arg) > 7
