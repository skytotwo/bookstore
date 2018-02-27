from django import forms


class RegisterForm(forms.Form):
    email = forms.CharField(
        required=True,
        label='',
        widget=forms.EmailInput(attrs={
            'id': 'inputEmail',
            'placeholder': '邮箱',
            'class': 'form-control'
        }))
    password = forms.CharField(
        required=True,
        label='',
        min_length=5,
        widget=forms.PasswordInput(attrs={
            'id': 'inputPassword',
            'placeholder': '密码',
            'class': 'form-control'
        }))
    repeat = forms.CharField(
        required=True,
        label='',
        min_length=5,
        widget=forms.PasswordInput(attrs={
            'id': 'repeatPassword',
            'placeholder': '确认密码',
            'class': 'form-control'
        }))

    def clean_repeat(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        repeat = cleaned_data.get('repeat')
        if password != repeat:
            raise forms.ValidationError('两次密码不一致')


class LoginForm(forms.Form):
    email = forms.CharField(
        required=True,
        label='',
        widget=forms.EmailInput(attrs={
            'id': 'inputEmail',
            'placeholder': '邮箱',
            'class': 'form-control'
        }))
    password = forms.CharField(
        required=True,
        label='',
        min_length=5,
        widget=forms.PasswordInput(attrs={
            'id': 'inputPassword',
            'placeholder': '密码',
            'class': 'form-control'
        }))
    remember = forms.BooleanField(
        required=False,
        label='',
        widget=forms.CheckboxInput(attrs={'id': 'remember'}))
