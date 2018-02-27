from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from ..users import models
from . import forms


class RegisterView(View):
    def get(self, request):
        register_form = forms.RegisterForm()
        return render(request, 'register.html',
                      {'register_form': register_form})

    def post(self, request):
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST.get('email', '')
            if models.UserProfile.objects.filter(email=username):
                messages.info(request, '该邮箱已注册')
                return render(request, 'register.html',
                              {'register_form': register_form})
            user_profile = models.UserProfile()
            user_profile.username = username
            user_profile.email = username
            user_profile.password = make_password(
                request.POST.get('password', ''))
            user_profile.save()
            messages.info(request, '注册成功，请登录')
            return HttpResponseRedirect(reverse('auth:login'))
        else:
            return render(request, 'register.html',
                          {'register_form': register_form})


class LoginView(View):
    def get(self, request):
        login_form = forms.LoginForm()
        redirect_url = request.GET.get('next', '')
        return render(request, 'login.html', {
            'login_form': login_form,
            'redirect_url': redirect_url
        })

    def post(self, request):
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user = authenticate(username=email, password=password)
            if user is not None:
                # 实现记住功能
                if request.POST.get('remember', ''):
                    request.session.set_expiry(60 * 60 * 24)
                login(request, user)
                redirect_url = request.POST.get('next', '')
                if redirect_url:
                    return HttpResponseRedirect(redirect_url)
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.info(request, '邮箱或密码错误，请重新登录')
                return render(request, 'login.html',
                              {'login_form': login_form})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))
