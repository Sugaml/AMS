from django.urls import path, include
from . import views
from django.contrib import admin
from apps.api import api as views
from apps.attendances import attendance as views




urlpatterns = [
      path("", include('apps.api.urls') ),
      path("attendance/", include('apps.attendances.urls') ),
]
admin.site.site_url = None
admin.site.site_header = 'SOMTU'
