from django import forms


class ChangePasswordForm(forms.Form):
    old_password = forms.PasswordInput()
    new_password = forms.PasswordInput()
    repeat = forms.PasswordInput()


class ChangeEmailForm(forms.Form):
    email = forms.EmailInput()
    password = forms.PasswordInput()


class ChangeUsernameForm(forms.Form):
    username = forms.CharField(required=True)


class RecipientForm(forms.Form):
    id = forms.IntegerField(required=False)
    name = forms.CharField()
    phone_number = forms.CharField(max_length=11)
    region = forms.CharField()
    address = forms.CharField()
    zip_code = forms.CharField(max_length=6)
    default = forms.BooleanField(required=False)


class OrderForm(forms.Form):
    recipient_id = forms.IntegerField()
    payment_method_id = forms.IntegerField()
