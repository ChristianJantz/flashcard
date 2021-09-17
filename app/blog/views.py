from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"


class AboutView(TemplateView):
    template_name = "about.html"
