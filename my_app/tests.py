from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomeTest(SimpleTestCase):
    def test_home_page_status(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_home_page(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'home.html')

class AboutTest(SimpleTestCase):
    def test_about_page_status(self):
        url = reverse('about')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_about_page(self):
        url = reverse('about')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'about.html')

class ServicesTest(SimpleTestCase):
    def test_services_page_status(self):
        url = reverse('services')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_services_page(self):
        url = reverse('services')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'services.html')