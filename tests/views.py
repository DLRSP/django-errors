"""Test's view for django-errors"""
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseNotAllowed,
    HttpResponseNotFound,
    HttpResponseServerError,
)
from django.views.decorators.http import require_http_methods


def test_view(request):
    """Test's view"""
    if request.method != "GET":
        return HttpResponseNotFound("404 view")
    return HttpResponse("Test view")


def test_view_400(request):
    """Test's view code 400"""
    return HttpResponseBadRequest("400 view")


def test_view_403(request):
    """Test's view code 403"""
    return HttpResponseForbidden("403 view")


@require_http_methods(["POST"])
def test_view_405(request):
    """Test's view code 405"""
    return HttpResponseNotAllowed("405 view")


def test_view_500(request):
    """Test's view code 400"""
    return HttpResponseServerError("500 view")
