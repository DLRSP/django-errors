"""Django Views for django-errors module"""
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _


class CustomViewIndexErrors(TemplateView):
    """Public Index Page. url: /"""
    template_name = "django_errors/index.html"


def custom_400(request, exception=None):
    """Custom Page for 400 error (Bad Request). url: /500"""
    error_msg = _("Bad Request")
    response = render(request, 'django_errors/400.html', {'messages': error_msg})
    response.status_code = 400
    return response


def custom_403(request, exception=None):
    """Custom Page for 403 error (Permission Denied). url: /403"""
    error_msg = _("Permission Denied")
    response = render(request, 'django_errors/403.html', {'messages': error_msg})
    response.status_code = 403
    return response


def custom_404(request, exception=None):
    """Custom Page for 404 error (Not Found). url: /404"""
    error_msg = _("Page Not Found")
    response = render(request, 'django_errors/404.html', {'messages': error_msg})
    response.status_code = 404
    return response


def custom_500(request):
    """Custom Page for 500 error (Internal Server Errors). url: /500"""
    error_msg = _("System Error")
    response = render(request, 'django_errors/500.html', {'messages': error_msg})
    response.status_code = 500
    return response
