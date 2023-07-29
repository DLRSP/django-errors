"""Test's view for django-errors"""
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@user_passes_test(lambda u: u.is_superuser)
def test_view_403_only_superuser(request):
    """Test's view code 403"""
    return HttpResponse("200 correct get output for superuser")


@require_http_methods(["GET"])
def test_view_405_only_get(request):
    """Test's view code 405"""
    return HttpResponse("200 correct get output")


@require_http_methods(["POST"])
def test_view_405_only_post(request):
    """Test's view code 405"""
    return HttpResponse("200 correct post output")
