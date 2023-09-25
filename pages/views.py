from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class PricingPageView(TemplateView):
    template_name = "pricing.html"

class TestimonialsPageView(TemplateView):
    template_name = "testimonials.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"