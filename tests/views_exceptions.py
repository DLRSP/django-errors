"""Test's view exceptions"""
from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.http import Http404


def test_exception_400(request):
    """Test's handle code 400 when raise SuspiciousOperation"""
    raise SuspiciousOperation


def test_exception_403(request):
    """Test's handle code 403 when raise PermissionDenied"""
    raise PermissionDenied


def test_exception_404(request):
    """Test's handle code 404 when raise Http404"""
    raise Http404
