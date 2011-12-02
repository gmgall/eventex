# -*- coding: utf-8 -*-
from django import forms
from subscriptions.models import Subscription
from django.utils.translation import ugettext as _
from django.core.validators import EMPTY_VALUES


class PhoneWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (
            forms.TextInput(attrs=attrs),
            forms.TextInput(attrs=attrs))
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if not value:
            return [None, None]
        return value.split('-')


class PhoneField(forms.MultiValueField):
    widget = PhoneWidget()

    def __init__(self, *args, **kwargs):
        fields = (
            forms.IntegerField(),
            forms.IntegerField())
        super(PhoneField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if not data_list:
            return ''
        if data_list[0] in EMPTY_VALUES:
            raise forms.ValidationError(u'DDD inválido.')
        if data_list[1] in EMPTY_VALUES:
            raise forms.ValidationError(u'Número inválido.')
        return '%s-%s' % tuple(data_list)


class SubscriptionForm(forms.ModelForm):
    phone = PhoneField(required=False)

    class Meta:
        model = Subscription
        exclude = ('created_at', 'paid', )

    def clean(self):
        super(SubscriptionForm, self).clean()

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise forms.ValidationError(_(u'Informe seu e-mail ou telefone.'))
        return self.cleaned_data

