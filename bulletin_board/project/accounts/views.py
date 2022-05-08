import random

from datetime import *
import pytz
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView
from project_files.settings import DEFAULT_FROM_EMAIL

from .forms import BaseRegisterForm, OneTimeCodeInputForm
from .models import AppUser, OneTimeCode


def clean_model(email):
    codes = OneTimeCode.objects.all()
    for code in codes:
        if code.email == email or datetime.now(pytz.utc) - code.datetime > timedelta(minutes=5):
            code.delete()


class RegisterView(FormView):
    """
    Страница регистрации пользователя. Валидирует данные формы,
    генерирует одноразовый код и отправляет его пользователю
    на email. Передает управление ActivationCodeView.
    """
    form_class = BaseRegisterForm
    template_name = 'signup.html'

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        clean_model(email)
        code = random.randint(100000, 999999)
        OneTimeCode.objects.create(email=email, code=code)
        send_mail('Код подтверждения',
                  f"Ваш код подтверждения для регистрации на портале:\n{str(code)}",
                  DEFAULT_FROM_EMAIL,
                  [email],
                  fail_silently=True)

        return HttpResponseRedirect(reverse('activation', kwargs={'email': email}))


class ActivationCodeView(FormView):
    """
    Проверяет правильность высланного кода, делает профиль пользователя
    активным, аутентифицирует и залогинивает его. Редирект на
    страницу профиля пользователя.
    """
    form_class = OneTimeCodeInputForm
    template_name = 'code_input_form.html'

    def get_success_url(self):
        return reverse('bulletins_list')

    def form_valid(self, form):
        code = form.cleaned_data.get('code')
        email = self.request.path.split('/')[-2]
        if OneTimeCode.objects.filter(email=email, code=code).exists():
            user = AppUser.objects.get(email=email)
            user.is_active = True
            user.save()
            login(self.request, user)
            messages.success(self.request, 'Добро пожаловать на сайт!')
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Неверный код! Попробуйте еще раз.')
            return HttpResponseRedirect(reverse('activation', kwargs={'email': email}))


class UserLogoutView(LogoutView):

    def get_next_page(self):
        self.next_page = self.request.GET.get('next', '')
        print(self.next_page)
        return super().get_next_page()
