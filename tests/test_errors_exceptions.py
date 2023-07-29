"""Unit Tests for the module"""
import logging

from django.test import TestCase

LOGGER = logging.getLogger(name="django-errors")


class ErrorsTestCase(TestCase):
    """Test Case for django-errors"""

    def setUp(self):
        """Set up common assets for tests"""
        LOGGER.debug("Tests setUp")

    def tearDown(self):
        """Remove Test Data"""
        LOGGER.debug("Tests tearDown")

    def test_400_exception_SuspiciousOperation(self):
        """Test the url of 400 page."""
        LOGGER.debug("400 Test raise exception SuspiciousOperation")
        response = self.client.get("/test-exception-400/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(400, response.status_code)
        self.assertTemplateUsed(response, "errors/400.html")

    def test_403_exception_PermissionDenied(self):
        """Test the url of 403 page."""
        LOGGER.debug("403 Test raise exception PermissionDenied")
        response = self.client.get("/test-exception-403/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(403, response.status_code)
        self.assertTemplateUsed(response, "errors/403.html")

    def test_404_exception_Http404(self):
        """Test the url of 404 page."""
        LOGGER.debug("404 raise exception Http404")
        response = self.client.get("/test-exception-404/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(404, response.status_code)
        self.assertTemplateUsed(response, "errors/404.html")

    def test_500_exception_InternalError(self):
        """Test the url of 500 page."""
        LOGGER.debug("500 Test raise exception InternalError")
        response = self.client.get("/500/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(500, response.status_code)
        self.assertTemplateUsed(response, "errors/500.html")

    # def test_X_redirect_urls(self):
    # """Test that redirects end urls"""
    # LOGGER.debug("Test X Redirect URLs")
    # response = self.client.get('/403/', follow=True)
    # self.assertRedirects(response, "http://testserver/admin/login/?next=/admin/")
