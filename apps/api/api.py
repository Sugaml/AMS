from django.views.generic import TemplateView
from decouple import config
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from apps.models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin,TemplateView):
    template_name = "apps/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = datetime.now()
        return context

    def get(self, request):
        user = request.user
        active_page="home"
        context = {
            "users": user,
            }
        return render(request, self.template_name, context)

     



class WelcomeView(TemplateView):
    template_name = "apps/welcome.html"

    def get(self, request):
        return render(request, self.template_name)
    
class LoginView(TemplateView):
    template_name = "apps/login.html"
    default_redirect = "/"

    # @method_decorator(login_required)
    def get(self, request):
        next = request.GET.get("next","/home/")
        return render(request, self.template_name)

    def post(self, request):
        next = request.POST.get("next","")
        if next == "/logout/":
            next = "/home/"
        username = request.POST["username"]
        password = request.POST["password"]
        print(username)
        user = User.objects.filter(username=username).first()
        print(user)
        if user:
            if not user.is_active:
                messages.error(
                    request, "Login failed ! user is deactivated."
                )
                return HttpResponseRedirect(f"/login/?next={next}")

            user = authenticate(username=username, password=password)
            if user and user.is_authenticated:
                login(request, user)
                if next:
                    return HttpResponseRedirect(next)
                return redirect("home_page")

            messages.error(
                request, "Login failed ! password do not match."
            )
        else:
            messages.error(
                request, "Login failed ! username do not match."
            )
        return HttpResponseRedirect(f"/login/?next={next}")