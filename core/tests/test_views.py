# coding=utf-8

from django.test import TestCase, Client
from django.urls import reverse

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')


    def tearDown(self):
        # remove o que tiver sido criado durante o teste
        pass

    def test_status_code(self):
        # remove o que tiver sido criado
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code,200)

    def test_template_used(self):

        response = self.client.get(self.url)
        self.assertTemplateUsed(response,'index.html')


