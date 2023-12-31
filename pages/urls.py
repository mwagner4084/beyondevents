from django.urls import path

from .views import (AboutPageView, ConfirmPageView, ContactPageView,
                    GalleryPageView, HomePageView, PricingPageView,
                    TestimonialsPageView)

urlpatterns = [
    path("confirm/", ConfirmPageView.as_view(), name="confirm"),
    path("gallery/", GalleryPageView.as_view(), name="gallery"),
    path("testimonials/", TestimonialsPageView.as_view(), name="testimonials"),
    path("pricing/", PricingPageView.as_view(), name="pricing"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]
