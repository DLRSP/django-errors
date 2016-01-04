"""Unit Tests for the Example module"""

# pylint: disable=R0904, C0103

from django.test import TestCase

from django.core.exceptions import ObjectDoesNotExist
import logging

LOGGER = logging.getLogger(name='example')


class ExampleTestCase(TestCase):
    """Test Case for Social Profile"""

    def setUp(self):
        """Set up common assets for tests"""
        LOGGER.debug("Example Tests setUp")

    def tearDown(self):
        """Remove Test Data"""
        LOGGER.debug("Example Tests tearDown")
		
    def test_400_urls(self):
        """Test the url of 400 page."""
        LOGGER.debug("400 Test Redirect URLs")
        response = self.client.get('/400/', follow=True)
        self.assertEqual(400, response.status_code)

    def test_403_urls(self):
        """Test the url of 403 page."""
        LOGGER.debug("403 Test Redirect URLs")
        response = self.client.get('/403/', follow=True)
        self.assertEqual(403, response.status_code)

    def test_404_urls(self):
        """Test the url of 404 page."""
        LOGGER.debug("404 Test URLs")
        response = self.client.get('/404/', follow=True)
        self.assertEqual(404, response.status_code)

    def test_404_urls(self):
        """Test that redirects kicking in when trying to go to 404 page."""
        LOGGER.debug("404 Test Redirect URLs")
        response = self.client.get('/UrlShouldNotExist/', follow=True)
        self.assertEqual(404, response.status_code)

    def test_500_urls(self):
        """Test the url of 500 page."""
        LOGGER.debug("500 Test Redirect URLs")
        response = self.client.get('/500/', follow=True)
        self.assertEqual(500, response.status_code)

    # def test_X_redirect_urls(self):
        # """Test that redirects end urls"""
        # LOGGER.debug("Test X Redirect URLs")
        # response = self.client.get('/403/', follow=True)
        # self.assertRedirects(response, "http://testserver/admin/login/?next=/admin/")

