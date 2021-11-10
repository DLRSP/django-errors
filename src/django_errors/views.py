"""Django Views for django-errors module"""
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError
from django.template import loader
from django.views.decorators.http import require_http_methods
from django.utils.translation import ugettext_lazy as _


@require_http_methods(["GET"])
def custom_400(request, exception=None):
    """Custom Page for 400 error (Bad Request). url: /400"""
    error_msg = _("Bad Request")
    t = loader.get_template('errors/400.html')
    c = {'messages': error_msg, 'exception': exception}
    return HttpResponseBadRequest(t.render(c, request))


@require_http_methods(["GET"])
def custom_403(request, exception=None):
    """Custom Page for 403 error (Permission Denied). url: /403"""
    error_msg = _("Permission Denied")
    t = loader.get_template('errors/403.html')
    c = {'messages': error_msg, 'exception': exception}
    return HttpResponseForbidden(t.render(c, request))


@require_http_methods(["GET"])
def custom_404(request, exception=None):
    """Custom Page for 404 error (Not Found). url: /404"""
    error_msg = _("Page Not Found")
    t = loader.get_template('errors/404.html')
    c = {'messages': error_msg, 'exception': exception}
    return HttpResponseNotFound(t.render(c, request))


@require_http_methods(["GET"])
def custom_500(request):
    """Custom Page for 500 error (Internal Server Errors). url: /500"""
    error_msg = _("System Error")
    t = loader.get_template('errors/500.html')
    c = {'messages': error_msg}
    return HttpResponseServerError(t.render(c, request))
