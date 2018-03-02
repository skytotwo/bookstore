from django import forms


class CartAddForm(forms.Form):
    quantity = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'id': 'quantity',
            'value': '1',
        }))
