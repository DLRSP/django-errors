"""Test's urls view for django-errors"""
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden,\
    HttpResponseNotAllowed, HttpResponseServerError, HttpResponse
from django.urls import path


def test_view(request):
    """Test's view"""
    if request.method != "GET":
        return HttpResponseNotFound("404 view")
    return HttpResponse("Test view")


urlpatterns = [
    path("", test_view),
    path("test-400/", HttpResponseBadRequest("400 view")),
    path("test-403/", HttpResponseForbidden("403 view")),
    path("test-405/", HttpResponseNotAllowed("POST", "405 view")),
    path("test-500/", HttpResponseServerError("500 view")),
]
