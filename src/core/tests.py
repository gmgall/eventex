from django.test import TestCase

class ViewsTest(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        self.assertTrue(response.context['quote'])
        self.assertTrue(response.context['credit'])
        self.assertEquals(response.status_code, 200)
