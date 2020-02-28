# Cart function gets values from the user
# Using a form will be useful to pass data to views.py


from django import forms


class AddProductForm(forms.Form):
    quantity = forms.IntegerField()
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

