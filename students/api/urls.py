from django.contrib import admin
from django.urls import path

from . import methods

urlpatterns = [
    path('login/', methods.login),
]