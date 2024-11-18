from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from main.models import Product

class ProductEntryForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['jersey_name', 'description', 'price', 'quantity']
    
    def clean_jersey_name(self):
        jersey_name = self.cleaned_data.get("jersey_name")
        # Check if the field is empty
        if not jersey_name:
            raise ValidationError("This field cannot be blank.")
        # Strip HTML tags for XSS protection
        return strip_tags(jersey_name)

    def clean_description(self):
        description = self.cleaned_data.get("description")
        # Check if the field is empty
        if not description:
            raise ValidationError("This field cannot be blank.")
        # Strip HTML tags for XSS protection
        return strip_tags(description)

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is None:
            raise ValidationError("This field cannot be blank.")
        return price

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        if quantity is None:
            raise ValidationError("This field cannot be blank.")
        return quantity
