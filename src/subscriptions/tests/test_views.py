from django.test import TestCase
from django.core.urlresolvers import reverse
from subscriptions.models import Subscription
from subscriptions.forms import SubscriptionForm


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
