from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
]
admin.site.site_url = None
admin.site.site_header = 'SOMTU'
