from django.test import TestCase
from subscriptions.forms import SubscriptionForm


class FormTest(TestCase):

    def test_subscription_ok(self):
        form = SubscriptionForm({
            'name': 'Guilherme Gall',
            'cpf': '12345678901',
            'email': 'gmgall@gmail.com',
            'phone_0': '24',
            'phone_1': '88499266',
        })
        self.assertTrue(form.is_valid())

    def test_subscription_without_name(self):
        form = SubscriptionForm({
            'name': '',
            'cpf': '12345678901',
            'email': 'gmgall@gmail.com',
            'phone_0': '24',
            'phone_1': '88499266',
        })
        self.assertFalse(form.is_valid())

    def test_subscription_without_cpf(self):
        form = SubscriptionForm({
            'name': 'Guilherme Gall',
            'cpf': '',
            'email': 'gmgall@gmail.com',
            'phone_0': '24',
            'phone_1': '88499266',
        })
        self.assertFalse(form.is_valid())

    def test_subscription_without_email(self):
        form = SubscriptionForm({
            'name': 'Guilherme Gall',
            'cpf': '12345678901',
            'email': '',
            'phone_0': '24',
            'phone_1': '88499266',
        })
        self.assertTrue(form.is_valid())

    def test_subscription_without_phone(self):
        form = SubscriptionForm({
            'name': 'Guilherme Gall',
            'cpf': '12345678901',
            'email': 'gmgall@gmail.com',
            'phone_0': '',
            'phone_1': ''
        })
        self.assertTrue(form.is_valid())
