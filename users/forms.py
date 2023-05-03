from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Div, Row


class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<h1 class="font-bold text-3xl pb-5 mb-8 border-b border-solid border-gray-700 ">Welcome!</h1>'),
            HTML('<label for="username" class="text-left block mb-1 text-sm font-medium text-gray-900 dark:text-white">Your username</label>'),
            Field("username", placeholder="caveman123", css_class="text-input mb-4"),
            HTML('<label for="email" class="text-left block mb-1 text-sm font-medium text-gray-900 dark:text-white">Your email</label>'),
            Field("email", placeholder="cave123@men.com", css_class="text-input mb-4"),
            HTML('<label for="password" class="text-left block mb-1 text-sm font-medium text-gray-900 dark:text-white">Your password</label>'),
            Field("password1", placeholder="#hi_mom8%$!", css_class="text-input mb-4"),
            HTML('<label for="password" class="text-left block mb-1 text-sm font-medium text-gray-900 dark:text-white">Confirm your password</label>'),
            Field("password2", placeholder="#hi_mom8%$!", css_class="text-input mb-4"),
            Div(
                Div(
                    HTML('<label for="first_name" class="text-left block mb-1 text-sm font-medium text-gray-900 dark:text-white">Your first name</label>'),
                    Field("first_name", placeholder="John", css_class="text-input mb-4")
                ),
                Div(
                    HTML('<label for="last_name" class="text-left block mb-1 text-sm font-medium text-gray-900 dark:text-white">Your last name</label>'),
                    Field("last_name", placeholder="Doe", css_class="text-input mb-4")
                ),
                css_class="flex gap-4 justify-between"
            ),
            Div(
                HTML("<button type='submit' class='text-white focus:outline-none focus:ring font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center bg-blue-600 hover:bg-blue-700 focus:ring-blue-800'>Register</button>"),
                HTML("<a class='text-white ml-auto focus:outline-none focus:ring font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center bg-blue-600 hover:bg-blue-700 focus:ring-blue-800' href='/user/login'>..or log-in!</a>"),
                css_class="flex mt-6"
            ),
        )
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None
        self.helper.form_show_labels = False
        self.helper.form_method = 'POST'

    class Meta:
        model = User
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
            HTML('<h1 class="font-bold text-3xl pb-5 mb-8 border-b border-solid border-gray-700 ">Welcome back!</h1>'),
            HTML('<label for="email" class="text-left block mb-1 text-sm font-medium text-gray-900 dark:text-white">Your email</label>'),
            Field("username", placeholder="your@gmail.com", css_class="text-input mb-4"),
            HTML('<label for="password" class="text-left block mb-1 text-sm font-medium text-gray-900 dark:text-white mb-4">Your password</label>'),
            Field("password", placeholder="Password", css_class="text-input"),
            Div(
                HTML("<button type='submit' class='text-white focus:outline-none focus:ring font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center bg-blue-600 hover:bg-blue-700 focus:ring-blue-800'>Login</button>"),
                HTML("<a class='text-white ml-auto focus:outline-none focus:ring font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center bg-blue-600 hover:bg-blue-700 focus:ring-blue-800' href='/user/sign-up'>Or join us!</a>"),
                css_class="flex mt-6"
            ),
        )
        self.helper.form_show_labels = False
        self.helper.label_class = 'text-white-800 text-lg'
        self.helper.form_method = 'POST'

    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]