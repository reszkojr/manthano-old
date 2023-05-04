from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views

import classrooms

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.log_in, name='log_in'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('logout/', views.log_out, name='log_out'),
    path('profile/', views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

