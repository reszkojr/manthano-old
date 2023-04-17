from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/user/login')
def home(request):
    return render(request, 'main/home.html')