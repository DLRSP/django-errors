"""Test's view for django-errors"""
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseNotAllowed, HttpResponseServerError, HttpResponse


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


def test_view_405(request):
    """Test's view code 405"""
    return HttpResponseNotAllowed("405 view")


def test_view_500(request):
    """Test's view code 400"""
    return HttpResponseServerError("500 view")
