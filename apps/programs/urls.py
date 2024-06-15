from django.urls import path
from apps.views import program_list, program_create, program_update, program_delete, program_toggle_active

urlpatterns = [
    path('', program_list, name='program_list'),
    path('create/', program_create, name='program_create'),
    path('<int:pk>/edit/', program_update, name='program_update'),
    path('<int:pk>/delete/', program_delete, name='program_delete'),
    path('<int:pk>/toggle/', program_toggle_active, name='program_toggle_active'),
]
