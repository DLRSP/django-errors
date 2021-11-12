"""Test's urls view for django-errors"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.test_view),
    path("test-400/", views.test_view_400),
    path("test-403/", views.test_view_403),
    path("test-405/", views.test_view_405),
    path("test-500/", views.test_view_500),
]
