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

    def test_400_urls(self):
        """Test the url of 400 page."""
        LOGGER.debug("400 Test Redirect URLs")
        response = self.client.get("/400/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(400, response.status_code)

    def test_403_urls(self):
        """Test the url of 403 page."""
        LOGGER.debug("403 Test Redirect URLs")
        response = self.client.get("/403/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(403, response.status_code)

    def test_404_urls(self):
        """Test the url of 404 page."""
        LOGGER.debug("404 Test URLs")
        response = self.client.get("/404/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(404, response.status_code)

    def test_not_exist_urls(self):
        """Test that redirects kicking in when trying to go to 404 page."""
        LOGGER.debug("404 Test Redirect URLs")
        response = self.client.get("/UrlShouldNotExist/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(404, response.status_code)

    def test_500_urls(self):
        """Test the url of 500 page."""
        LOGGER.debug("500 Test Redirect URLs")
        response = self.client.get("/500/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(500, response.status_code)
        self.assertTemplateUsed(response, "errors/500.html")
