from django import forms

class SubscriptionForm(forms.Form):
    email_address = forms.EmailField(label="Enter Your Email ", max_length=200)