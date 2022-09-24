from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from .backend import EmailBackend
from django.contrib.auth.models import User
from .models import Discord


def log_in(request):
    """Log_in page"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = EmailBackend().authenticate(
                request,
                username=email,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'user_management/login.html', {'form': form})


def sign_up(request):
    """sign_up page"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data['email']
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            discord_id = request.POST.get('discord_id')
            username = f"{first_name}_{last_name}"
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            new_user = User.objects.get(email=email)
            discord = Discord(
                user=new_user,
                discord_id=discord_id
            )
            discord.save()
            return redirect('log_in')
    else:
        form = SignUpForm()
    return render(request, 'user_management/signup.html', {'form': form})


@login_required
def log_out(request):
    logout(request)
    return redirect('/')
