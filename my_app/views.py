from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    # process this request (home req)
    template_name = 'home.html'


class AboutPageView(TemplateView):
    # process this request (home req)
    template_name = 'about.html'

class ServicesPageView(TemplateView):
    template_name = 'services.html'