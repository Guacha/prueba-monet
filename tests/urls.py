from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('mytests/', views.get_tests, name="mytests"),
]