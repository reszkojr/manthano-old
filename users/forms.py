from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import Student

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, Submit, HTML, Div, Button


class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user_icon = '<i class="fa-solid fa-user" style="color: #bec8da;"></i>'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field("first_name", placeholder="First name", css_class="text-input"),
                Field("last_name", placeholder="Last name", css_class="text-input"),
                Field("username", placeholder="Username", css_class="text-input"),
                Field("email", placeholder="E-mail", css_class="text-input"),
                Field("password1", placeholder="Password", css_class="text-input"),
                Field("password2", placeholder="Password confirmation", css_class="text-input"),
                Div(
                    HTML("<a class='ml-auto' href='/login'>Already have an account?</a>"),
                    css_class="flex mt-12"
                ),
                css_class="w-1/2 mx-auto"
            ),
        )
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None
        self.helper.form_show_labels = False
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
            Div(
                Field("username", placeholder="E-mail", css_class="text-input"),
                Field("password", placeholder="Password", css_class="text-input"),
                Div(
                    HTML("<input class='cursor-pointer' type='submit' value='Login'>"),
                    HTML("<a class='ml-auto' href='/sign_up'>Don't have an account?</a>"),
                    css_class="flex mt-12"
                ),
                css_class="w-1/2 mx-auto"
            ),
        )
        self.helper.form_show_labels = False
        self.helper.label_class = 'text-white-800 text-lg'
        self.helper.form_method = 'POST'

    class Meta:
        model = Student
        fields = [
            "username",
            "password",
        ]