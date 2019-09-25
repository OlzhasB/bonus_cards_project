import re
from django.db import models
from datetime import datetime
from django.forms.utils import ValidationError
from django.utils import timezone

class Card(models.Model):
    class Meta:
        db_table = 'card'
    series = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    dateOfIssue = models.DateTimeField(verbose_name='Date of Issue', default=datetime.now)
    dateOfExpiration = models.DateTimeField(verbose_name='Date of Expiration')
    totalSum = models.DecimalField(decimal_places=2, max_digits=9)
    active = models.BooleanField()
    datetime = timezone.now()

    def __str__(self):
        return f'{self.series} card with number {self.number}'

    def clean(self, *args, **kwargs):
        if not re.fullmatch('[0-9][0-9][0-9][0-9] [0-9][0-9][0-9][0-9]', self.number):
            raise ValidationError('Type a card number in a correct format!')

        if self.dateOfExpiration < self.dateOfIssue:
            raise ValidationError('Date of expiration must be later than the date of issue!')

        if self.dateOfExpiration < timezone.now() and self.active:
            raise ValidationError('This card is expired! It cant be active!')

        if self.dateOfIssue > timezone.now() and self.active:
            raise ValidationError('Date of issue cant be later than now!')

# Возьмите меня на работу, я быстро учусь :)

        return super(Card, self).clean(*args, **kwargs)