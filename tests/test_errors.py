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

    def test_not_exist_urls(self):
        """Test that redirects kicking in when trying to go to 404 page."""
        LOGGER.debug("404 Test URL not exist")
        response = self.client.get("/UrlShouldNotExist/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(404, response.status_code)
        self.assertTemplateUsed(response, "errors/404.html")

    def test_page_auth_protected(self):
        """Test that redirects kicking in when trying to go to a page Auth protected."""
        LOGGER.debug("Test URL accept only get")
        response = self.client.get("/admin/", follow=True)
        LOGGER.debug(response)
        # todo: test auth protected: NOT_AUTHORIZED (should be 401)
        # self.assertEqual(403, response.status_code)
        # self.assertTemplateUsed(response, 'errors/403.html')
        self.assertRedirects(response, "/admin/login/?next=%2Fadmin%2F")

    def test_page_without_privileges(self):
        """Test that redirects kicking in when trying to go to a page Auth protected."""
        LOGGER.debug("Test URL accept only get")
        response = self.client.get("/admin/", follow=True)
        LOGGER.debug(response)
        # todo: test auth protected: NOT_AUTHORIZED (should be 401)
        # self.assertEqual(403, response.status_code)
        # self.assertTemplateUsed(response, 'errors/403.html')
        self.assertRedirects(response, "/admin/login/?next=%2Fadmin%2F")

    # def test_X_redirect_urls(self):
    #     """Test that redirects end urls"""
    #     LOGGER.debug("Test X Redirect URLs")
    #     response = self.client.get('/403/', follow=True)
    #     self.assertRedirects(response, "http://testserver/admin/login/?next=/admin/")

    def test_method_not_allowed_get(self):
        """Test that redirects kicking in when trying
        to use method GET on view accept only POST."""
        LOGGER.debug("Test URL accept only get")
        response = self.client.get("/test-method-only-post/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(405, response.status_code)
        self.assertTemplateUsed(response, "errors/405.html")

    def test_method_not_allowed_post(self):
        """Test that redirects kicking in when trying
        to use method POST on view accept only GET."""
        LOGGER.debug("Test URL accept only get")
        response = self.client.post("/test-method-only-get/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(405, response.status_code)
        self.assertTemplateUsed(response, "errors/405.html")
