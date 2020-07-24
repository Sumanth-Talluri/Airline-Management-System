from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


# view for index
def index(request):
    # first we should check if the user is authenticated or not
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "users/user.html")


# view for login page
def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        # this will return the user of it is authenticated
        user = authenticate(request, username=username, password=password)
        # checking if user is authenticated
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        # if authentication failed
        else:
            return render(request, "users/login.html", {
                "message": "Invalid Credentials"
            })
    # if GET
    return render(request, "users/login.html")


# view for logging out
def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged Out!"
    })
