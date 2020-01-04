"""
    Django Errors URL Pattern List.
"""

# pylint: disable=W0401, W0614, E1120

from django.conf.urls import url
from django.views.decorators.cache import never_cache
from . import views

urlpatterns = [
	url(r'^$', never_cache(views.CustomView_IndexErrors.as_view()),name="all_errors"),
	url(r'^403', views.custom_403, name="403"),
	url(r'^404', views.custom_404, name="404"),
	url(r'^400', never_cache(views.custom_400), name="400"),
	url(r'^500', never_cache(views.custom_500), name="500"),
]

handler400 = views.custom_400
""" Handle 400 error """

handler403 = views.custom_403
""" Handle 403 error """

handler404 = views.custom_404
""" Handle 404 error """

handler500 = views.custom_500
""" Handle 500 error """

