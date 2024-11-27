from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Register View
def Register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('Username')
        password = request.POST.get('password')

        if username == "":
            messages.info(request, 'Please provide username')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists')
            return redirect('register')

        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('login')

    return render(request, 'register.html')

# Login View
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Please provide all the fields')
            return redirect('login')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Please register first')
            return redirect('login')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

        login(request, user)
        messages.success(request, 'Logged in successfully')
        return redirect('dashboard')

    return render(request, 'login.html')

# Dashboard View
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')