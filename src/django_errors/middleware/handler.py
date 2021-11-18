"""Django App's middleware for django-errors app"""
from django.conf import settings
from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _


class HttpResponseNotAllowedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if isinstance(response, HttpResponseNotAllowed):
            error = _("Method Not Allowed")
            error_msg = _(
                "Sorry, the used method is not allowed for the page with that URL."
            )
            context = {
                "error": error,
                "error_code": 405,
                "error_message": f"{error_msg} ({request.method})",
                "error_request_method": request.method,
                "exception": None,
            }
            return render(
                request,
                getattr(
                    settings,
                    "TEMPLATE_ERROR_405",
                    getattr(settings, "TEMPLATE_ERROR_ALL", "errors/405.html"),
                ),
                context=context,
                status=405,
            )

        return response

    # def process_view(request, view_func, view_args, view_kwargs):
    #     # This code is executed just before the view is called
    #
    # def process_exception(request, exception):
    #     # This code is executed if an exception is raised
    #
    # def process_template_response(request, response):
    #     # This code is executed if the response contains a render() method
