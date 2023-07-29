"""Test's urls view for django-errors"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.i18n import JavaScriptCatalog

from src.django_errors import views as errors_views

from . import views, views_exceptions, views_standard, views_templates

urlpatterns = [
    path("", include("django_errors.urls")),
    path("admin/", admin.site.urls),
    path("test-method-only-get/", views.test_view_405_only_get),
    path("test-method-only-post/", views.test_view_405_only_post),
    path("test-exception-400/", views_exceptions.test_exception_400),
    path("test-exception-403/", views_exceptions.test_exception_403),
    path("test-exception-404/", views_exceptions.test_exception_404),
    path("test-template-400/", views_templates.test_template_400),
    path("test-template-403/", views_templates.test_template_403),
    path("test-template-404/", views_templates.test_template_404),
    path("test-template-500/", views_templates.test_template_500),
    path("test-standard-400/", views_standard.test_view_400),
    path("test-standard-403/", views_standard.test_view_403),
    path("test-standard-404/", views_standard.test_view_404),
    path("test-standard-405/", views_standard.test_view_405),
    path("test-standard-410/", views_standard.test_view_410),
    path("test-standard-500/", views_standard.test_view_500),
]

urlpatterns += i18n_patterns(
    re_path(r"^jsi18n/$", JavaScriptCatalog.as_view(), name="javascript-catalog"),
    path("", include("django_errors.urls")),
    path("test-method-only-get/", views.test_view_405_only_get),
    path("test-method-only-post/", views.test_view_405_only_post),
    path("test-exception-400/", views_exceptions.test_exception_400),
    path("test-exception-403/", views_exceptions.test_exception_403),
    path("test-exception-404/", views_exceptions.test_exception_404),
    path("test-template-400/", views_templates.test_template_400),
    path("test-template-403/", views_templates.test_template_403),
    path("test-template-404/", views_templates.test_template_404),
    path("test-template-500/", views_templates.test_template_500),
    path("test-standard-400/", views_standard.test_view_400),
    path("test-standard-403/", views_standard.test_view_403),
    path("test-standard-404/", views_standard.test_view_404),
    path("test-standard-405/", views_standard.test_view_405),
    path("test-standard-410/", views_standard.test_view_410),
    path("test-standard-500/", views_standard.test_view_500),
)


# @># Server Errors Handlers
handler400 = errors_views.custom_400
""" Handle 400 error """

handler403 = errors_views.custom_403
""" Handle 403 error """

handler404 = errors_views.custom_404
""" Handle 404 error """

handler500 = errors_views.custom_500
""" Handle 500 error """
