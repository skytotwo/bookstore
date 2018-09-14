from django.http import Http404
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from . import models as user_models
from apps.manages import models as manage_models
from . import forms as user_forms


# 设置
@login_required
class SettingsView(View):
    def get(self, request):
        recipients = user_models.Recipient.objects.all()
        recipient_form = user_forms.RecipientForm()
        change_username_form = user_forms.ChangeUsernameForm()
        change_password_form = user_forms.ChangePasswordForm()
        change_email_form = user_forms.ChangeEmailForm()
        return render(
            request, 'settings.html', {
                'recipients': recipients,
                'recipient_form': recipient_form,
                'change_username_form': change_username_form,
                'change_password_form': change_password_form,
                'change_email_form': change_email_form
            })

    def post(self, request, option):
        post = request.POST
        # 设置中的表单
        recipients = user_models.Recipient.objects.all()
        recipient_form = user_forms.RecipientForm(post)
        change_username_form = user_forms.ChangeUsernameForm(post)
        change_password_form = user_forms.ChangePasswordForm(post)
        change_email_form = user_forms.ChangeEmailForm(post)

        if option == 'update-recipient':  # 更新地址
            if recipient_form.is_valid():
                recipient = user_models.Recipient.objects.get(
                    id=post.get('id'))
                recipient.name = post.get('name')
                recipient.phone_number = post.get('phone_number')
                recipient.region = post.get('region')
                recipient.address = post.get('address')
                recipient.zip_code = post.get('zip_code')
                recipient.default = bool(post.get('default'))
                recipient.save()
                messages.info(request, '地址修改成功')
            else:
                messages.info(request, recipient_form.errors)
        elif option == 'add-recipient':  # 添加地址
            if recipient_form.is_valid():
                recipient = user_models.Recipient()
                recipient.user = request.user
                recipient.name = post.get('name')
                recipient.phone_number = post.get('phone_number')
                recipient.region = post.get('region')
                recipient.address = post.get('address')
                recipient.zip_code = post.get('zip_code')
                recipient.default = bool(post.get('default'))
                recipient.save()
                messages.info(request, '地址添加成功')
            else:
                messages.info(request, recipient_form.errors)
        elif option == 'change-username':  # 修改昵称
            if change_username_form.is_valid():
                request.user.username = change_username_form.username.data
                messages.info(request, '昵称修改成功')
            else:
                messages.info(request, '昵称修改失败，请重试')
        elif option == 'change-password':  # 更改密码
            if change_password_form.is_valid():
                request.user.set_password(change_password_form.password.data)
                messages.info(request, '密码更改成功')
            else:
                messages.info(request, '密码更改失败，请重试')
        elif option == 'change-email':  # 更改邮箱
            if change_email_form.is_valid():
                messages.info(request, '认证邮件已经发送，请登录你的邮箱进行确认')
            else:
                messages.info(request, '邮箱更改失败，请重试')
        else:
            raise Http404

        return render(
            request, 'settings.html', {
                'recipients': recipients,
                'recipient_form': recipient_form,
                'change_username_form': change_username_form,
                'change_password_form': change_password_form,
                'change_email_form': change_email_form
            })


# 订单
@login_required
class OrderView(View):
    def get(self, request):
        processing_orders = request.user.get_processing_orders()
        finished_orders = request.user.get_finished_orders()
        return render(
            request, 'order.html', {
                'processing_orders': processing_orders,
                'finished_orders': finished_orders,
            })

    def post(self, request):
        post = request.POST
        order_form = user_forms.OrderForm(post)
        if order_form.is_valid():
            user = request.user
            user_models.Order.create(
                user=user,
                recipient=user.recipient.get(id=post.get('recipient_id')),
                items=user.cart.get_checked_items(),
                payment_method=manage_models.Payment.objects.get(
                    id=post.get('payment_method_id')),
                payment_amount=user.cart.get_checked_total_price())
            # 将购物车中已经下单的图书移除
            user.cart.remove_checked_items()
            return HttpResponseRedirect(reverse('user:order'))
        else:
            messages.info(request, '表单验证失败')
            return render(
                request,
                'settlement.html',
            )


# 提交订单
@login_required
def confirm_order(request, order_id):
    request.user.order.get(id=order_id).confirm()
    return HttpResponseRedirect(reverse('user:order'))
