"""Test's urls view for django-errors"""
from django.urls import path
from views import *

urlpatterns = [
    path("", test_view),
    path("test-400/", test_view_400),
    path("test-403/", test_view_403),
    path("test-405/", test_view_405),
    path("test-500/", test_view_500),
]
