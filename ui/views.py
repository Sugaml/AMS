from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your views here.


@login_required
def index(request):
    if request.user.is_teacher:
        return render(request, 'ui/t_homepage.html')
    if request.user.is_student:
        return render(request, 'ui/homepage.html')
    if request.user.is_superuser:
        return render(request, 'ui/admin_page.html')
    return render(request, 'ui/logout.html')