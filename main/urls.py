from django.urls import path, include
from django.contrib.auth import views as auth_views

import classrooms

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('classroom', include('classrooms.urls')),
]
