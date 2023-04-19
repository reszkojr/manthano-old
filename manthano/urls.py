from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('user/', include('users.urls', namespace='users')),
    path('class/', include('classrooms.urls', namespace='class')),
    path("__reload__/", include("django_browser_reload.urls")),
]
