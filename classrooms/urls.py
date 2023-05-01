from django.urls import path, include

from . import views

app_name = 'class'

urlpatterns = [
    path('room/<slug:code>/', views.classroom, name='classroom'),
    path('create/', views.create_classroom, name='create_classroom'),
]