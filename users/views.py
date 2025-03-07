from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect based on role
            if user.role == "student":
                 return redirect("student_list")
            elif user.role == "teacher":
                return redirect("all-teachers")
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, "users/login.html")

def user_register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        role = request.POST.get("role")  # Get role from form

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Check if email already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect("register")

        # Create user without requiring a username
        user = CustomUser.objects.create_user(
            email=email, password=password, first_name=first_name, last_name=last_name, role=role
        )
        user.save()

        messages.success(request, "Account created successfully. You can now log in.")
        return redirect("login")

    return render(request, "users/register.html")

def user_logout(request):
    logout(request)
    return redirect("login")  # Redirect to login page

