import datetime
from django.test import TestCase
from django.core.urlresolvers import reverse
from core.models import Speaker, Talk

class ViewTest(TestCase):

    def setUp(self):
        self.s = Speaker.objects.create(
            name = 'Guilherme Gall',
            slug = 'guilherme-gall',
            url = 'http://gmgall.wordpress.com/'
        )
        self.s.contact_set.create(kind='E', value='gmgall@gmail.com')

        self.t = Talk.objects.create(
            title = 'Palestra',
            start_time = datetime.datetime.now()
        )
        self.t.speakers.add(self.s)

    def test_homepage(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        self.assertTrue(response.context['quote'])
        self.assertTrue(response.context['credit'])
        self.assertEquals(response.status_code, 200)

    def test_show_speaker_detail(self):
        response = self.client.get(reverse('core:speaker_detail',
            args=[self.s.slug]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/speaker_detail.html')

    def test_show_talks(self):
        response = self.client.get(reverse('core:talks'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/talks.html')

    def test_show_talk_detail(self):
        response = self.client.get(reverse('core:talk_detail', args=[1]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/talk_detail.html')
        self.assertContains(response, self.t.title)
        self.assertContains(response, self.s.name)
