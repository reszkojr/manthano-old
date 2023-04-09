from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import RegistrationForm

@login_required(login_url='/login')
def home(request):
    return render(request, 'main/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {'form': form})