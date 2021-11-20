from django.shortcuts import render
from django.views.generic import TemplateView,ListView

# Create your views here.

class BaseView(TemplateView):
    template_name = "base.html"


class HomeView(TemplateView):
    template_name = "home.html"


class AboutUsView(TemplateView):
    template_name = "aboutus.html"

class ThingListView(ListView):
    template_name = "things.html"
    model='Thing'

