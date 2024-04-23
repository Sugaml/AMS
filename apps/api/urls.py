from django.urls import path
from . import api as views


urlpatterns = [
    path("", views.WelcomeView.as_view(), name="home_page"),
]