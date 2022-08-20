from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .backend import EmailBackend
from django.contrib.auth.models import User
from .models import Discord
from random import choice
from string import ascii_letters


def log_in(request):
    if request.method == 'POST':
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
            return None
    return render(request, 'user_management/login.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print('form')
        if form.is_valid():
            print('form is ok')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data['email']
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            discord_id = form.cleaned_data.get('discord_id')
            username_fake = ''.join([choice(ascii_letters) for i in range(30)])
            user = User.objects.create_user(
                username=username_fake,
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
        print('form not ok')
        form =SignUpForm()
    return render(request, 'user_management/signup.html', {'form': form})


@login_required
def log_out(request):
    log_out(request)
    return redirect('/')
