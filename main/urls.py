from django.urls import path

import classrooms

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('classroom', classrooms.views.join_classroom, name='sign_up'),
]