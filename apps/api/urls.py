from django.urls import path
from . import api as views


urlpatterns = [
    path("", views.WelcomeView.as_view(), name="home_page"),
    path("login/", views.LoginView.as_view(), name="log_in_page"),
]