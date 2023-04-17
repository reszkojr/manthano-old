from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import Student

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, Submit, HTML, Div, Button


class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                "first_name", "last_name", css_class="flex flex-row justify-between"),
            "username",
            "email",
            "password1",
            "password2",
            Div(
                HTML("<a href=\"/login\">Already have an account?</a>"),
                Submit('submit', 'Register', css_class=""),
                css_class="flex flex-row justify-between"
            )
        )
        self.helper.label_class = 'text-white-800 text-lg'
        self.helper.form_method = 'POST'

    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "username",
            "password",
            Div(
                HTML("<a href=\"/register\"> Don't have an account?</a>"),
                Submit('submit', 'Login', css_class=""),
                css_class="flex flex-row justify-between"
            )
        )
        self.helper.label_class = 'text-white-800 text-lg'
        self.helper.form_method = 'POST'

    class Meta:
        model = Student
        fields = [
            "username",
            "password",
        ]