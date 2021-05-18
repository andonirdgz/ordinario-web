# from django.shortcuts import render
from django.views.generic import TemplateView

# def home(request):
#     return render(request, 'core/home.html')
class HomeView(TemplateView):
    template_name = 'core/home.html'

# def about(request):
#     return render(request, 'core/about.html')

class AboutView(TemplateView):
    template_name = 'core/about.html'


# def contact(request):
#     return render(request, 'core/contact.html')
class ContactView(TemplateView):
    template_name = 'core/contact.html'
