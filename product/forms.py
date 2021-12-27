from django import forms
from django.db.models import forms
from . import models


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order_in
        fields = '__all__'