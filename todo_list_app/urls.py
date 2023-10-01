from django.contrib import admin
from django.urls import path, include
from rest_framework import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),
    path("",include("rest_framework.urls"))
]
