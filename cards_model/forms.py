from django import forms
from .models import Card


SERIES_LIST = [('', ''),
               ('Gold', 'Gold'),
               ('Platinum', 'Platinum'),
               ('Silver', 'Silver')
               ]
ACTIVE_LIST = [('', ''),
               ('True', 'Active'),
               ('False', 'Not active'),
               ]


class CardForm(forms.ModelForm):
    number = forms.CharField(label='Card number',
                             widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'XXXX XXXX'}))

    series = forms.CharField(label='Series',
                             widget=forms.Select(choices=SERIES_LIST))

    active = forms.CharField(label='Status',
                             widget=forms.Select(choices=ACTIVE_LIST))

    dateOfExpiration = forms.DateTimeField(label='Date of Expiration',
                                           widget=forms.TextInput(
                                               attrs={'class': 'form-control',
                                                      'placeholder': 'YYYY-MM-DD HH:MM:SS'}))

    totalSum = forms.DecimalField(label='Total Sum',
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control',
                                             'placeholder': 'Number with max digits: 9'}))

    class Meta(object):
        model = Card
        fields = ('number', 'series', 'dateOfIssue', 'dateOfExpiration', 'totalSum', 'active')


class CardSearchForm(forms.Form):
    number = forms.CharField(
                             required=False,
                             label='Card number',
                             widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': 'XXXX XXXX'})
                  )

    series = forms.CharField(
                    required=False,
                    label='Series',
                    widget=forms.Select(choices=SERIES_LIST)
                  )

    active = forms.CharField(
                    required=False,
                    label='Status',
                    widget=forms.Select(choices=ACTIVE_LIST)
                  )



class CardGenerateForm(forms.Form):
     series = forms.CharField(label='Series', widget=forms.Select(choices=SERIES_LIST))
     amount = forms.IntegerField(label='Amount', min_value=1, max_value=10)
     period = forms.IntegerField(label='Period(Month)', min_value=1, max_value=12)
