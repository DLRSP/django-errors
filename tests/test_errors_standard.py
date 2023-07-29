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

    def test_400_standard(self):
        """Test the url of 400 page."""
        LOGGER.debug("400 Test Standard view overwrite")
        response = self.client.get("/400/", follow=True)
        response_standard = self.client.get("/test-standard-400/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(type(response), type(response_standard))
        self.assertEqual(response.status_code, response_standard.status_code)
        self.assertTemplateUsed(response, "errors/400.html")

    def test_403_standard(self):
        """Test the url of 403 page."""
        LOGGER.debug("403 Test Redirect URLs")
        response = self.client.get("/403/", follow=True)
        response_standard = self.client.get("/test-standard-403/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(type(response), type(response_standard))
        self.assertEqual(response.status_code, response_standard.status_code)
        self.assertTemplateUsed(response, "errors/403.html")

    def test_404_standard(self):
        """Test the url of 404 page."""
        LOGGER.debug("404 Test URLs")
        response = self.client.get("/404/", follow=True)
        response_standard = self.client.get("/test-standard-404/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(type(response), type(response_standard))
        self.assertEqual(response.status_code, response_standard.status_code)
        self.assertTemplateUsed(response, "errors/404.html")

    def test_405_standard(self):
        """Test the url of 404 page."""
        LOGGER.debug("405 Test GET URLs with only POST")
        response = self.client.post("/400/", follow=True)
        response_standard = self.client.get("/test-standard-405/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(type(response), type(response_standard))
        self.assertEqual(response.status_code, response_standard.status_code)
        self.assertTemplateUsed(response, "errors/405.html")

    def test_500_standard(self):
        """Test the url of 500 page."""
        LOGGER.debug("500 Test Redirect URLs")
        response = self.client.get("/500/", follow=True)
        response_standard = self.client.get("/test-standard-500/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(type(response), type(response_standard))
        self.assertEqual(response.status_code, response_standard.status_code)
        self.assertTemplateUsed(response, "errors/500.html")
