from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from ..users import models
from . import forms
import base64


# 注册
class RegisterView(View):
    def get(self, request):
        register_form = forms.RegisterForm()
        return render(request, 'register.html',
                      {'register_form': register_form})

    def post(self, request):
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            cd = register_form.cleaned_data
            username = cd['email']  # email作为初始用户名
            # 检查邮箱是否已经注册
            if models.UserProfile.objects.filter(email=username):
                messages.info(request, '该邮箱已注册')
                return render(request, 'register.html',
                              {'register_form': register_form})
            # 新建用户
            user_profile = models.UserProfile()
            user_profile.username = username
            user_profile.email = username
            user_profile.password = make_password(cd['password'])
            user_profile.save()
            messages.info(request, '注册成功，请登录')
            return HttpResponseRedirect(reverse('auth:login'))
        # 如果表单验证不通过则返回该表单
        return render(request, 'register.html', {'register_form': register_form})


# 验证码图片
def validate_code(request):
    from ..utils.validate_code import generate_validate_code
    img, code = generate_validate_code()
    request.session['validate_code'] = code
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    img.save(buf, 'gif')
    # 将内存中的图片数据返回给客户端，MIME类型为图片gif
    return HttpResponse(buf.getvalue(), 'image/gif')


# 登录
class LoginView(View):
    def get(self, request):
        login_form = forms.LoginForm()
        redirect_url = request.GET.get('next', '')
        public_key = self.generate_key(request)  # 生成密钥保存到session中
        return render(request, 'login.html', {
            'login_form': login_form,
            'redirect_url': redirect_url,
            'public_key': public_key
        })

    def post(self, request):
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            # 首先检查验证码
            validate_code = request.session['validate_code']
            comfimed_code = cd['validate_code']
            print(validate_code)
            print(comfimed_code)
            if validate_code != comfimed_code:
                messages.info(request, '验证码错误')
            # 再检查用户
            else:
                user = authenticate(username=cd['email'],
                                    password=self.decrypt(request, cd['password']))  # 验证是否匹配
                if user is not None:
                    # 实现记住功能
                    if cd['remember']:
                        request.session.set_expiry(60 * 60 * 24)
                    login(request, user)
                    redirect_url = request.POST.get('next', '')
                    if redirect_url:
                        return HttpResponseRedirect(redirect_url)
                    return HttpResponseRedirect(reverse('index'))
                messages.info(request, '邮箱或密码错误，请重新登录')
            return render(request, 'login.html', {'login_form': login_form})
        return render(request, 'login.html', {
            'login_form': login_form,
            'public_key': request.session['public_key']
        })

    def generate_key(self, request):
        # 生成密钥
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)
        public_key = key.publickey().exportKey()
        private_key = key.exportKey()
        # 将密钥解析成字符串，保存到session
        request.session['private_key'] = bytes.decode(private_key)
        request.session['public_key'] = bytes.decode(public_key)
        return request.session['public_key']

    def decrypt(self, request, password):
        confirmed_password = base64.b64decode(password)
        private_key = request.session['private_key']
        private_key = RSA.import_key(private_key)
        cipher_rsa2 = PKCS1_v1_5.new(private_key)
        data = cipher_rsa2.decrypt(confirmed_password, None)
        password = bytes.decode(data)
        return password


# 登出
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))
