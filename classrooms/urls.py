from django.urls import path, include

from . import views

urlpatterns = [
    path('classroom', views.join_classroom, name='joinclassroom')
]