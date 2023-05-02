from django.urls import path

from .views import GoogleLogin, LogoutView, OTPView, google_view

urlpatterns = [

    path('login/google', GoogleLogin.as_view(), name='google-rest'),
    path('logout', LogoutView.as_view()),
    path('accounts/google/login/callback/', google_view),
    path('otp', OTPView.as_view())
]
