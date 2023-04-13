from django.urls import path, include

import classrooms

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('classroom', include('classrooms.urls')),
]
