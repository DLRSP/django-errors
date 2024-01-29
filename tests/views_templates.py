"""Test's view for django-errors"""

from django_errors.views import custom_400, custom_403, custom_404, custom_500


def test_template_400(request):
    """Test's template code 400"""
    return custom_400(request)
    # return render(request, "errors/400.html", status=400)


def test_template_403(request):
    """Test's template code 403"""
    return custom_403(request)
    # return render(request, "errors/403.html", status=403)


def test_template_404(request):
    """Test's template code 404"""
    return custom_404(request)
    # return render(request, "errors/404.html", status=404)


def test_template_500(request):
    """Test's template code 500"""
    return custom_500(request)
    # return render(request, "errors/500.html", status=500)
