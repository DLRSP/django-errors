"""
    Django Errors URL Pattern List.
"""

from django.urls import re_path
from django.views.decorators.cache import never_cache

from . import views

urlpatterns = [
    re_path(r"^400/", never_cache(views.custom_400), name="400"),
    re_path(r"^403/", views.custom_403, name="403"),
    re_path(r"^404/", views.custom_404, name="404"),
    re_path(r"^500/", never_cache(views.custom_500), name="500"),
]
