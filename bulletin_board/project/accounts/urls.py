from django.contrib.auth.views import LoginView
from django.urls import path, include

from .views import RegisterView, ActivationCodeView, UserLogoutView

urlpatterns = [
    path("login/", LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signup/activation/<str:email>/', ActivationCodeView.as_view(), name='activation'),
    path('', include('django.contrib.auth.urls')),
]
