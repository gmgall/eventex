from django.test import TestCase
from django.db import IntegrityError
from subscriptions.models import Subscription


class ModelTest(TestCase):

    def setUp(self):
        self.s = Subscription(
                name = 'Guilherme Gall',
                cpf = '12345678901',
                email = 'gmgall@gmail.com',
                phone = '24-88499266'
        )
        self.s.save()

    def test_create_new_subscription(self):
        self.assertEquals(self.s.id, 1)

    def test_remove_subscription(self):
        self.s.delete()
        self.assertRaises(Subscription.DoesNotExist, Subscription.objects.get,
                pk=self.s.id)

    def test_cpf_must_be_unique(self):
        s2 = Subscription(
                name = 'Gregory House',
                cpf = '12345678901',
                email = 'house@ppth.edu',
                phone = '1 609 123456789'
        )
        self.assertRaises(IntegrityError, s2.save)

    def test_email_must_be_unique(self):
        s2 = Subscription(
                name = 'Gregory House',
                cpf = '01234567890',
                email = 'gmgall@gmail.com',
                phone = ''
        )
        self.assertRaises(IntegrityError, s2.save)