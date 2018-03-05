from django import forms


class CartAddForm(forms.Form):
    quantity = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'id': 'quantity',
            'value': '1',
        }))


class SettlementForm(forms.Form):
    recipient_id = forms.CharField(required=True, label='')
    payment_method = forms.CharField(required=True, label='')

    # from apps.manages.models import Payment
    # recipient = forms.ChoiceField(required=True, label='', choices=[])
    # payment_method = forms.ChoiceField(
    #     required=True,
    #     label='',
    #     choices=Payment.objects.all().values_list('id', 'name'))
    #
    # def __init__(self, user, *args, **kwargs):
    #     super(SettlementForm, self).__init__(*args, **kwargs)
    #     self.fields['recipient'].choices = user.recipient.all().values_list(
    #         'id', 'name')
