"""Django Views for django-errors module"""
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext

class CustomView_IndexErrors(TemplateView):
    """Public Index Page. url: /"""
    template_name = "django_errors/index.html"

def custom_400(request):
    """Custom Page for 400 error (Bad Request). url: /500"""
    error_msg = "Bad Request"
    response = render_to_response('django_errors/400.html',
							{'messages': error_msg},
							context_instance=RequestContext(request))
    response.status_code = 400
    return response
	
def custom_403(request):
    """Custom Page for 403 error (Permission Denied). url: /403"""
    error_msg = "Permission Denied"
    response = render_to_response('django_errors/403.html',
							{'messages': error_msg},
							context_instance=RequestContext(request))
    response.status_code = 403
    return response
	
def custom_404(request):
    """Custom Page for 404 error (Not Found). url: /404"""
    error_msg = "Page Not Found"
    response = render_to_response('django_errors/404.html',
							{'messages': error_msg},
							context_instance=RequestContext(request))
    response.status_code = 404
    return response
	
def custom_500(request):
    """Custom Page for 500 error (Internal Server Errors). url: /500"""
    error_msg = "System Error"
    response = render_to_response('django_errors/500.html',
							{'messages': error_msg},
							context_instance=RequestContext(request))
    response.status_code = 500
    return response

