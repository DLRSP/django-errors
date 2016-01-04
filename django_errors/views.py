""" Django Views for django-errors module """
from django.shortcuts import render
from django.views.generic import TemplateView

class CustomView_IndexErrors(TemplateView):
    """ Public Index Page. url: / """
    template_name = "django_errors/index.html"

def custom_400(request):
    """ Custom Page for 400 error (Bad Request). url: /500 """
    error_msg = "Bad Request"
    return render(request, 'django_errors/400.html', {'error_msg': error_msg})
	
def custom_403(request):
    """ Custom Page for 403 error (Permission Denied). url: /403 """
    return render(request, 'django_errors/403.html')

def custom_404(request):
    """ Custom Page for 404 error (Not Found). url: /404 """
    return render(request, 'django_errors/404.html')
	
def custom_500(request):
    """ Custom Page for 500 error. url: /500 """
    error_msg = "System Error"
    return render(request, 'django_errors/500.html', {'error_msg': error_msg})