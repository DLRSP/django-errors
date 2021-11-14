"""Django Views for django-errors module"""
from django.http import (
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseNotFound,
    HttpResponseServerError,
)
from django.template import loader
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def custom_400(request, exception=None):
    """Custom Page for 400 error (Bad Request). url: /400"""
    error_msg = _("Bad Request")
    template = loader.get_template("errors/400.html")
    context = {"messages": error_msg, "exception": exception}
    return HttpResponseBadRequest(template.render(context, request))


@require_http_methods(["GET"])
def custom_403(request, exception=None):
    """Custom Page for 403 error (Permission Denied). url: /403"""
    error_msg = _("Permission Denied")
    template = loader.get_template("errors/403.html")
    context = {"messages": error_msg, "exception": exception}
    return HttpResponseForbidden(template.render(context, request))


@require_http_methods(["GET"])
def custom_404(request, exception=None):
    """Custom Page for 404 error (Not Found). url: /404"""
    error_msg = _("Page Not Found")
    template = loader.get_template("errors/404.html")
    context = {"messages": error_msg, "exception": exception}
    return HttpResponseNotFound(template.render(context, request))


@require_http_methods(["GET"])
def custom_500(request, exception=None):
    """Custom Page for 500 error (Internal Server Errors). url: /500"""
    error_msg = _("System Error")
    template = loader.get_template("errors/500.html")
    context = {"messages": error_msg, "exception": exception}
    return HttpResponseServerError(template.render(context, request))
