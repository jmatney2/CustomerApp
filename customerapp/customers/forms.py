"""Forms for the Customers app"""

from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    """Form for adding customers"""

    class Meta:
        model = Customer
        fields = "__all__"
