from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm
from .models import User

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('products:product_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('products:product_list')
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('products:product_list')

def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'accounts/profile.html', {'profile_user': user})

@login_required
def follow(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    if request.user != user_to_follow:
        if request.user in user_to_follow.followers.all():
            user_to_follow.followers.remove(request.user)
        else:
            user_to_follow.followers.add(request.user)
    return redirect('accounts:profile', username=username)