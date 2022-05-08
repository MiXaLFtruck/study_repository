from django.contrib.auth.forms import UserCreationForm
from django.forms import Form

from .models import AppUser
from django import forms
from django.utils.translation import gettext_lazy as _


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", help_text='Обязательное поле')
    first_name = forms.CharField(label=_("First Name"), required=False)
    last_name = forms.CharField(label=_("Last Name"), required=False)

    class Meta:
        model = AppUser
        fields = ("email",
                  "username",
                  "first_name",
                  "last_name",
                  "password1",
                  "password2", )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
        return user


class OneTimeCodeInputForm(Form):
    code = forms.IntegerField(label=_('The Code'))
