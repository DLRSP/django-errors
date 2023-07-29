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

    def test_400_template_locale_it(self):
        """Test the url of 400 page."""
        LOGGER.debug("400 Test URLs")
        response = self.client.get("/it/test-template-400/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(400, response.status_code)
        self.assertContains(response, b"Brutta Richiesta", status_code=400, count=2)

    def test_403_template_locale_it(self):
        """Test the url of 403 page."""
        LOGGER.debug("403 Test URLs")
        response = self.client.get("/it/test-template-403/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(403, response.status_code)
        self.assertTemplateUsed(response, "errors/403.html")
        self.assertContains(response, b"Permesso Negato", status_code=403, count=2)
        self.assertContains(
            response,
            b"Non hai il permesso per vedere questa pagina!",
            status_code=403,
            count=1,
        )

    def test_404_template_locale_it(self):
        """Test the url of 404 page."""
        LOGGER.debug("404 Test URLs")
        response = self.client.get("/it/test-template-404/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(404, response.status_code)
        self.assertContains(response, b"Pagina non trovata", status_code=404, count=2)

    def test_not_exist_urls_locale_it(self):
        """Test that redirects kicking in when trying to go to 404 page."""
        LOGGER.debug("404 Test Redirect URLs")
        response = self.client.get("/it/UrlShouldNotExist/", follow=True)
        LOGGER.debug(response)
        print(response.content)
        self.assertEqual(404, response.status_code)
        self.assertContains(response, b"Pagina non trovata", status_code=404, count=2)

    def test_405_template_get_locale_it(self):
        """Test the url of 405 page."""
        LOGGER.debug("405 Test URLs")
        response = self.client.post("/it/test-method-only-get/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(405, response.status_code)
        print(response.content)
        self.assertContains(
            response, b"Metodo non consentito (POST)[405]", status_code=405, count=1
        )
        self.assertContains(
            response, b"Metodo non consentito (POST)", status_code=405, count=2
        )
        self.assertContains(
            response,
            b"Scusa, il metodo usato non \xc3\xa8 consentito per la pagina con questo URL.",
            status_code=405,
            count=1,
        )

    def test_405_template_post_locale_it(self):
        """Test the url of 405 page."""
        LOGGER.debug("405 Test URLs")
        response = self.client.get("/it/test-method-only-post/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(405, response.status_code)
        self.assertContains(
            response, b"Metodo non consentito (GET)[405]", status_code=405, count=1
        )
        self.assertContains(
            response, b"Metodo non consentito (GET)", status_code=405, count=2
        )
        self.assertContains(
            response,
            b"Scusa, il metodo usato non \xc3\xa8 consentito per la pagina con questo URL.",
            status_code=405,
            count=1,
        )

    def test_500_template_locale_it(self):
        """Test the url of 400 page."""
        LOGGER.debug("500 Test URLs")
        response = self.client.get("/it/test-template-500/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(500, response.status_code)
        self.assertTemplateUsed(response, "errors/500.html")
        self.assertContains(
            response, b"Errore Interno del Server", status_code=500, count=2
        )
