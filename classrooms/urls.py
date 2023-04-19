from django.urls import path, include

from . import views

app_name = 'class'

urlpatterns = [
    path('', views.join_classroom, name='join_classroom'),
    path('create/', views.create_classroom, name='create_classroom'),
]