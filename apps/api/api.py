from django.views.generic import TemplateView
from decouple import config
from django.shortcuts import render, redirect



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