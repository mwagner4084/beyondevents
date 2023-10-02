from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    """ Contact Model """
    fname = models.CharField(max_length=254, null=True, blank=True)
    lname = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=254, null=True, blank=True)
    location = models.CharField(max_length=254, null=True, blank=True)
    wedding_date = models.DateField(auto_now_add=True)
    comments = models.CharField(max_length=500, null=True, blank=True)
    referred_by = models.CharField(max_length=254, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    notes = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return f"{self.lname}, {self.fname}"

    def get_absolute_url(self):
        return reverse("contact", args=(self.pk))
