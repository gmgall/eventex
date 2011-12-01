from django.test import TestCase
from django.db import IntegrityError
from django.core.urlresolvers import reverse
from subscriptions.models import Subscription
from subscriptions.forms import SubscriptionForm

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

class ViewTest(TestCase):
    def test_success_subscription(self):
        # DB must be empty
        self.assertFalse(Subscription.objects.all())
        # POSTing a subscription
        response = self.client.post(reverse('subscriptions:subscribe'), {
            'name': 'Guilherme Gall',
            'cpf': '12345678901',
            'email': 'gmgall@gmail.com',
            'phone': '24-88499266'
        })
        # asserting the redirect after the subscription
        self.assertRedirects(response, reverse('subscriptions:success', args=[1]))
        # DB must have 1 item
        self.assertTrue(Subscription.objects.get(pk=1))

    def test_show_form(self):
        response = self.client.get(reverse('subscriptions:subscribe'))
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.context['form'], SubscriptionForm)
