from django.urls import path, include
from django.contrib.auth import views as auth_views

import classrooms

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
]
