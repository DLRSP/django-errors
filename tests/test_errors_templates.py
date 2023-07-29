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

    def test_400_template(self):
        """Test the url of 400 page."""
        LOGGER.debug("400 Test URLs")
        response = self.client.get("/test-template-400/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(400, response.status_code)
        self.assertTemplateUsed(response, "errors/400.html")
        self.assertContains(response, b"Bad Request", status_code=400, count=2)
        self.assertContains(
            response,
            b"The request could not be understood by the server due to "
            b"malformed syntax.",
            status_code=400,
            count=1,
        )

    def test_403_template(self):
        """Test the url of 403 page."""
        LOGGER.debug("403 Test URLs")
        response = self.client.get("/test-template-403/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(403, response.status_code)
        self.assertTemplateUsed(response, "errors/403.html")
        self.assertContains(response, b"Permission Denied", status_code=403, count=2)
        self.assertContains(
            response,
            b"You don&#x27;t have permissions to see this page!",
            status_code=403,
            count=1,
        )

    def test_404_template(self):
        """Test the url of 404 page."""
        LOGGER.debug("404 Test URLs")
        response = self.client.get("/test-template-404/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(404, response.status_code)
        self.assertTemplateUsed(response, "errors/404.html")
        self.assertContains(response, b"Page Not Found", status_code=404, count=2)
        print(response.content)
        self.assertContains(
            response,
            b"Sorry, we don&#x27;t have a page with that URL.",
            status_code=404,
            count=1,
        )

    def test_405_template_get(self):
        """Test the url of 405 page."""
        LOGGER.debug("405 Test URLs")
        response = self.client.get("/test-method-only-post/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(405, response.status_code)
        self.assertTemplateUsed(response, "errors/405.html")
        self.assertContains(
            response, b"Method Not Allowed (GET)[405]", status_code=405, count=1
        )
        self.assertContains(
            response, b"Method Not Allowed (GET)", status_code=405, count=2
        )
        self.assertContains(
            response,
            b"Sorry, the used method is not allowed for the page with that URL.",
            status_code=405,
            count=1,
        )

    def test_405_template_post(self):
        """Test the url of 405 page."""
        LOGGER.debug("405 Test URLs")
        response = self.client.post("/test-method-only-get/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(405, response.status_code)
        self.assertTemplateUsed(response, "errors/405.html")
        self.assertContains(
            response, b"Method Not Allowed (POST)[405]", status_code=405, count=1
        )
        self.assertContains(
            response, b"Method Not Allowed (POST)", status_code=405, count=2
        )
        self.assertContains(
            response,
            b"Sorry, the used method is not allowed for the page with that URL.",
            status_code=405,
            count=1,
        )

    def test_500_template(self):
        """Test the url of 400 page."""
        LOGGER.debug("500 Test URLs")
        response = self.client.get("/test-template-500/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(500, response.status_code)
        self.assertTemplateUsed(response, "errors/500.html")
        self.assertContains(
            response, b"Internal Server Error", status_code=500, count=2
        )
        self.assertContains(
            response,
            b"Sorry, an error has occurred with the application.",
            status_code=500,
            count=1,
        )
