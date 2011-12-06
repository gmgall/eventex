from django.test import TestCase
from django.core.urlresolvers import reverse
from core.models import Speaker

class ViewTest(TestCase):

    def setUp(self):
        s = Speaker.objects.create(
            name = 'Guilherme Gall',
            slug = 'guilherme-gall',
            url = 'http://gmgall.wordpress.com/'
        )
        s.contact_set.create(kind='E', value='gmgall@gmail.com')

    def test_homepage(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        self.assertTrue(response.context['quote'])
        self.assertTrue(response.context['credit'])
        self.assertEquals(response.status_code, 200)

    def test_show_speaker_detail(self):
        response = self.client.get(reverse('core:speaker_detail',
            args=['guilherme-gall']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/speaker_detail.html')
