from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from decimal import Decimal
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import login
from collections import Counter
from .forms import UserProfileForm


def user_login(request):  
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,
                                     password=password)
            if user:
                auth.login(request, user) 
                return redirect(reverse('cases:cases_view'))
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form, 'active_page': 'login'})


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'users/login.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'users/login.html')

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email format.")
            return render(request, 'users/login.html')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'users/login.html')

        if len(password1) < 8:
            messages.error(request, "Password should be at least 8 characters long.")
            return render(request, 'users/login.html')

        if not any(char.isdigit() for char in password1):
            messages.error(request, "Password should contain at least one number.")
            return render(request, 'users/login.html')

        if not any(char.islower() for char in password1) or not any(char.isupper() for char in password1):
            messages.error(request, "Password should contain both uppercase and lowercase letters.")
            return render(request, 'users/login.html')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        login(request, user) 

        return redirect('cases:cases_view')

    return render(request, 'users/login.html')

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)


    purchased_cases_list = [
        {"name": case_name, "quantity": quantity}
        for case_name, quantity in profile.purchased_cases.items()
    ]

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'users/profile.html', {
        'form': form,
        'profile': profile,
        'purchased_cases_list': purchased_cases_list,  
        'active_page': 'profile'
    })

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('cases:cases')


def get_money(request):
    if request.method == 'POST':
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            return HttpResponse("Profile does not exist", status=404)


        profile.balance += Decimal('150.00')
        profile.save()

    return render(request, 'users/profile.html', {'profile': profile})
