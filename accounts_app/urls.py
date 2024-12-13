from django.urls import path
from accounts_app.views import register_api_view, email_verification

urlpatterns = [
    path("register/", register_api_view, name="register"),
    path("verify-email/", email_verification, name="verify_email"),
]
