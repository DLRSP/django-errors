from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponse
from django.urls import path


def test_view(request):
    if request.method != "GET":
        return HttpResponseNotFound("Test 404 view")
    return HttpResponse("Test view")


def test_view_http400(request):
    return HttpResponseBadRequest("Test 400 view")


def test_view_http403(request):
    return HttpResponseForbidden("Test 403 view")


def test_view_http405(request):
    return HttpResponseNotAllowed("POST", "Test 405 view")


urlpatterns = [
    path("", test_view),
    path("test-400/", test_view_http400),
    path("test-403/", test_view_http403),
    path("test-405/", test_view_http403),
]
