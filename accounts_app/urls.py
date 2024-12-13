from django.urls import path
from accounts_app.views import register_api_view
urlpatterns = [
    path('register/', register_api_view, name="register")
]
