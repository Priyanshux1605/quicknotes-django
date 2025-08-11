from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username","").strip()
        password = request.POST.get("password","")
        # checking username and password
        if not username or not password:
            return render(request, "accounts/signup.html",
                          {"error": "Username and password are required."})
        if User.objects.filter(username=username).exists():
            return render(request, "accounts/signup.html",
                          {"error": "User already exist."})
        # create user 
        user = User.objects.create_user(username=username, password=password)
        login(request, user)                 # start session
        return redirect("notes-list")        # go to your notes page
    return render(request, "accounts/signup.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username","").strip()
        password = request.POST.get("password","")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("notes-list")
        return render(request, "accounts/login.html",
                      {"error": "Invalid username or password."})
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)                          # end session for the user
    return redirect("home")                 # back to homepage after logout
