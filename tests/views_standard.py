"""Test's view for django-errors"""
from django.http import (
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseGone,
    HttpResponseNotAllowed,
    HttpResponseNotFound,
    HttpResponseServerError,
)
from django.views.decorators.http import require_http_methods


def test_view_400(request):
    """Test's view code 400"""
    return HttpResponseBadRequest()


def test_view_403(request):
    """Test's view code 403"""
    return HttpResponseForbidden()


def test_view_404(request):
    """Test's view code 404"""
    return HttpResponseNotFound()


@require_http_methods(["POST"])
def test_view_405(request):
    """Test's view code 405"""
    return HttpResponseNotAllowed(["POST"])


def test_view_410(request):
    """Test's view code 410"""
    return HttpResponseGone()


def test_view_500(request):
    """Test's view code 500"""
    return HttpResponseServerError()
