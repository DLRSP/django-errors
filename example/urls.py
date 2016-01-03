"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from views import CustomIndex, Test404

from django_errors.views import custom_400, custom_403, custom_404, custom_500
""" Impot Custom Errors Views """

urlpatterns = [
    url(r'^$', CustomIndex.as_view(),name="index"),
    url(r'^admin/', admin.site.urls),
	
    url(r'^django_errors/', include('django_errors.urls')),
	
    url(r'^400/$', custom_400,name="400"),
    url(r'^403/$', custom_403,name="403"),
    url(r'^404/$', custom_404,name="404"),
    url(r'^500/$', custom_500,name="500"),
]

# handler404 = 'django_errors.views.custom_404'
""" Handle 404 also with DEBUG = True """

# handler500 = 'django_errors.views.custom_500'
""" Handle 500 also with DEBUG = True """

#TBD: handler403 = 'mysite.views.my_custom_permission_denied_view'
""" Handle 500 also with DEBUG = True """

#TBD: handler400 = 'mysite.views.my_custom_bad_request_view'
""" Handle 500 also with DEBUG = True """

