from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse

# from apps.core.utils import ajax_paginator

from .forms import UserRegisterForm, UserLoginForm, ProfileForm
from .models import Profile
from .services.validate_email_service import get_email_validate
from .services.validate_username_service import get_username_validate


def validate_username(request):
    """ Проверка доступности логина """
    response = {'username_taken': get_username_validate(request)}
    return JsonResponse(response)


def validate_email(request):
    """ Проверка доступности e-mail """
    response = {'email_taken': get_email_validate(request)}
    return JsonResponse(response)


class RegisterForm(SuccessMessageMixin, CreateView):
    """ Страница регистрации """
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')
    success_message = '%(username)s, добро пожаловать!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_profile'] = True
        return context

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


class LoginForm(SuccessMessageMixin, LoginView):
    """ Страница авторизации """
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    success_message = '%(username)s, добро пожаловать!'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_profile'] = True
        return context


class LogOutForm(LogoutView):
    """ Выход  """
    template_name = 'accounts/logout.html'
    success_url = reverse_lazy('logout')


class ProfileView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ Страница профиль пользователя """
    model = Profile
    template_name = 'accounts/profile/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    success_message = 'Профиль обновлён'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_profile'] = True
        return context

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse("profile", kwargs={'pk': pk})

    def form_valid(self, form):
        form.save()
        response = {'status': 'ok'}
        return JsonResponse(response, status=200)

    def form_invalid(self, form):
        response = {'status': 'error'}
        return JsonResponse(response, status=400)
