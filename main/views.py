from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import RegistrationForm

@login_required(login_url='/login')
def home(request):
    return render(request, 'main/home.html')