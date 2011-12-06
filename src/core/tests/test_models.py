from django.test import TestCase
from django.db import IntegrityError
from core.models import Speaker


class ModelTest(TestCase):

    def setUp(self):
        self.s = Speaker.objects.create(
            name = 'Guilherme Gall',
            slug = 'guilherme-gall',
            url = 'http://gmgall.wordpress.com/'
        )
        self.s.contact_set.create(kind='E', value='gmgall@gmail.com')

    def test_create_new_speaker(self):
        self.assertEquals(self.s.id, 1)

    def test_remove_speaker(self):
        self.s.delete()
        self.assertRaises(Speaker.DoesNotExist, Speaker.objects.get,
                pk=self.s.id)

    def test_slug_must_be_unique(self):
        s2 = Speaker(
            name = 'Gregory House',
            slug = 'guilherme-gall',
            url = 'http://ppth.edu',
        )
        self.assertRaises(IntegrityError, s2.save)
