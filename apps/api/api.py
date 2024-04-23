from django.views.generic import TemplateView
from decouple import config
from django.shortcuts import render, redirect



class WelcomeView(TemplateView):
    template_name = "apps/welcome.html"

    def get(self, request):
        return render(request, self.template_name)
    
