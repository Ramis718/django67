from django import forms
from django import forms
from django.db.models import fields
from . import models


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order_in
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer_in
        fields =['name', 'phone', 'email']