from django import forms


class SettlementForm(forms.Form):
    from apps.manages.models import Payment
    recipient = forms.ChoiceField(required=True, label='', choices=[])
    payment_method = forms.ChoiceField(
        required=True,
        label='',
        choices=Payment.objects.all().values_list('id', 'name'))

    def __init__(self, user, *args, **kwargs):
        super(SettlementForm, self).__init__(*args, **kwargs)
        self.fields['recipient'].choices = user.recipient.all().values_list(
            'id', 'name')


class TestForm(forms.Form):
    test = forms.CharField()
