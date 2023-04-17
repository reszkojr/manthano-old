from django.urls import path, include
from django.contrib.auth import views as auth_views

import classrooms

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('sign-up', views.sign_up, name='sign_up'),
]
