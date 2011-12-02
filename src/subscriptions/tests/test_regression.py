from django.test import TestCase
from django import forms
from subscriptions.forms import PhoneField


class RegressionPhoneFieldTest(TestCase):
    
    def test_empty_phone_field_should_result_in_empty_string(self):
        # Cria um form simples para o teste.
        class Form(forms.Form):
            phone = PhoneField(required=False)

        form = Form({})
        self.assertTrue(form.is_valid())
        self.assertDictEqual({'phone': ''}, form.cleaned_data)
