from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from utils.decorators import login_required_message_and_redirect


@login_required_message_and_redirect
def home(request):
    return render(request, 'home.html', {'nav': 'home'})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, f"You are now logged in as {user}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in')
        return redirect('home')
    login_form = AuthenticationForm(
        initial={'username': 'omar'})  # Pre filled username for demo
    messages.info(request, 'Hello their ! login using username: omar and password: omar')
    return render(request, 'login.html', context={'login_form': login_form, 'nav': 'login'})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')
        print(form.errors)
        messages.error(request, 'Unsuccessful registration')
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in')
        return redirect('home')
    form = RegisterForm()
    return render(request, 'register.html', context={'register_form': form, 'nav': 'register'})


@login_required_message_and_redirect(redirect_field_name=None)
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")


@login_required_message_and_redirect
def profile_view(request):
    return render(request, 'profile.html', context={'nav': 'profile'})


@login_required_message_and_redirect
def profile_edit_view(request):
    form = ProfileForm(instance=request.user, data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your details has been saved')
        return redirect('profile')
    return render(request, 'edit_profile.html', context={'nav': 'profile', 'edit_profile_form': form})


@login_required_message_and_redirect
def password_change_view(request):
    form = PasswordChangeForm(user=request.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        messages.success(request, 'Password has been changed successfully')
        return redirect('profile')
    return render(request, 'password_change.html', context={'nav': 'profile', 'password_form': form})
