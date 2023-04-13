from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Student

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

