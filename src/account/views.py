from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,
    PasswordResetView)
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import UserLoginForm, UserCreationForm, UserChangeForm
from system.mixins import AdminRequiredMixin
from .mixins import LogoutRequiredMixin, AdminSameRequiredMixin
from django_otp.forms import OTPAuthenticationForm
from .models import User
from django.utils.translation import gettext_lazy as _

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'account/form_.html'
    redirect_authenticated_user = False
    extra_context = {'title' : _("User Login")}
    # authentication_form=OTPAuthenticationForm

class UserCreateView(LogoutRequiredMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account:signin')
    extra_context = {'title' : _("User Signup")}



class UserLogoutView(LogoutView):
    template_name = 'account/logout.html'
    redirect_authenticated_user = True


class UserUpdateView(AdminSameRequiredMixin, UpdateView):
    next_page = reverse_lazy('account:signin')
    model = User
    form_class = UserChangeForm
    template_name = 'account/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_success_url(self):
        messages.success(self.request, 'Your Profile Update success.')
        return reverse_lazy('account:update', kwargs={'username': self.request.user.username})


class UserPasswordResetView(LogoutRequiredMixin, PasswordResetView):
    email_template_name = 'account/password_reset_email.html'
    # extra_email_context = None
    # from_email = None
    # html_email_template_name = None
    success_url = reverse_lazy('system:home')
    template_name = 'account/password_reset_form.html'
    # title = 'Password reset'
    # token_generator = default_token_generator

class UserPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('system:home')
    template_name = 'account/password_change_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Your Password Change success.')
        return '/'

class UserPasswordResetConfirmView(LogoutRequiredMixin, PasswordResetConfirmView):
    post_reset_login = False
    success_url = reverse_lazy('system:home')
    template_name = 'account/password_reset_confirm.html'


class UserPasswordResetDoneView(LogoutRequiredMixin, PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'



class UserPasswordResetCompleteView(LogoutRequiredMixin, PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'




class UserPasswordChangeDoneView(LogoutRequiredMixin, PasswordChangeDoneView):
    template_name = 'account/password_change_done.html'



def test(request, token):
    if token == 'ji-set':
        return HttpResponse('hello ' + token)
    return HttpResponseRedirect(request.path.replace(token, 'ji-set'))
