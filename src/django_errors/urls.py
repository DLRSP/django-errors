"""
    Django Errors URL Pattern List.
"""

from django.conf.urls import url
from django.views.decorators.cache import never_cache

from . import views

urlpatterns = [
    url(r"^403", views.custom_403, name="403"),
    url(r"^404", views.custom_404, name="404"),
    url(r"^400", never_cache(views.custom_400), name="400"),
    url(r"^500", never_cache(views.custom_500), name="500"),
]
