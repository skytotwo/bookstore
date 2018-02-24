from django.shortcuts import render
from django.views.generic.base import View
from . import forms


class RegisterView(View):
    def get(self, request):
        register_form = forms.RegisterForm()
        return render(request, 'register.html',
                      {'register_form': register_form})
