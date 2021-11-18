"""Django Views for django-errors module"""
from django.conf import settings
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
    error = _("Bad Request")
    error_msg = _(
        "The request could not be understood by the server due to malformed syntax."
    )
    template = loader.get_template(
        getattr(
            settings,
            "TEMPLATE_ERROR_400",
            getattr(settings, "TEMPLATE_ERROR_ALL", "errors/400.html"),
        )
    )
    context = {
        "error": error,
        "error_code": 400,
        "error_message": error_msg,
        "error_request_method": request.method,
        "exception": exception,
    }
    return HttpResponseBadRequest(template.render(context, request))


@require_http_methods(["GET"])
def custom_403(request, exception=None):
    """Custom Page for 403 error (Permission Denied). url: /403"""
    error = _("Permission Denied")
    error_msg = _("You don't have permissions to see this page!")
    template = loader.get_template(
        getattr(
            settings,
            "TEMPLATE_ERROR_403",
            getattr(settings, "TEMPLATE_ERROR_ALL", "errors/403.html"),
        )
    )
    context = {
        "error": error,
        "error_code": 403,
        "error_message": error_msg,
        "error_request_method": request.method,
        "exception": exception,
    }
    return HttpResponseForbidden(template.render(context, request))


@require_http_methods(["GET"])
def custom_404(request, exception=None):
    """Custom Page for 404 error (Not Found). url: /404"""
    error = _("Page Not Found")
    error_msg = _("Sorry, we don't have a page with that URL.")
    template = loader.get_template(
        getattr(
            settings,
            "TEMPLATE_ERROR_404",
            getattr(settings, "TEMPLATE_ERROR_ALL", "errors/404.html"),
        )
    )
    context = {
        "error": error,
        "error_code": 404,
        "error_message": error_msg,
        "error_request_method": request.method,
        "exception": exception,
    }
    return HttpResponseNotFound(template.render(context, request))


@require_http_methods(["GET"])
def custom_500(request, exception=None):
    """Custom Page for 500 error (Internal Server Error). url: /500"""
    error = _("Internal Server Error")
    error_msg = _("Sorry, an error has occurred with the application.")
    template = loader.get_template(
        getattr(
            settings,
            "TEMPLATE_ERROR_500",
            getattr(settings, "TEMPLATE_ERROR_ALL", "errors/500.html"),
        )
    )
    context = {
        "error": error,
        "error_code": 500,
        "error_message": error_msg,
        "error_request_method": request.method,
        "exception": exception,
    }
    return HttpResponseServerError(template.render(context, request))
