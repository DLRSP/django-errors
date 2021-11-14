"""Django App's middleware for django-errors app"""
from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

# Reference:
# https://stackoverflow.com/questions/49162214/why-django-doesnt-have-error-page-handler-for-405-method-not-allowed
# https://medium.com/scalereal/everything-you-need-to-know-about-middleware-in-django-2a3bd3853cd6
# https://dev.to/bikramjeetsingh/a-comprehensive-guide-to-django-middleware-2fee


class HttpResponseNotAllowedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if isinstance(response, HttpResponseNotAllowed):
            error_msg = _("Method Not Allowed")
            context = {"messages": f"{error_msg} ({request.method})", "exception": None}
            return render(request, "errors/405.html", context=context, status=405)

        return response

    # def process_view(request, view_func, view_args, view_kwargs):
    #     # This code is executed just before the view is called
    #
    # def process_exception(request, exception):
    #     # This code is executed if an exception is raised
    #
    # def process_template_response(request, response):
    #     # This code is executed if the response contains a render() method
