import smtplib
from email.mime.text import MIMEText

from django import forms
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.db import IntegrityError
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from pages.forms import ContactForm

from .models import Contact


class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class PricingPageView(TemplateView):
    template_name = "pricing.html"

class RentalsPageView(TemplateView):
    template_name = "rentals.html"

class TestimonialsPageView(TemplateView):
    template_name = "testimonials.html"


class GalleryPageView(TemplateView):
    template_name = "gallery.html"


class ContactPageView(TemplateView):
    handle = 'contact'
    template_name = "contact.html"
    form = ContactForm

    def __init__(self, *args, **kwargs):
        if not self.handle or not self.template_name:
            raise Exception('You must define a handle and template_name')

    def get_context_data(self, **kwargs):
        """ Add the page to the context. """
        context = super(TemplateView, self).get_context_data(**kwargs)

        if self.form:
            context['form'] = self.form
            context['tag'] = "div"
            context['wrapper_class'] = "form-group"

        self.context = context

        return context

    def send_custom_email(self, subject, message, from_email, to_email):
        # Initialize connection
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()

        email_host_user = settings.EMAIL_HOST_USER
        email_host_password = settings.EMAIL_HOST_PASSWORD
        smtp_server.login(email_host_user, email_host_password)

        # Create email
        msg = MIMEText(message)
        msg['From'] = from_email
        msg['To'] = ', '.join(to_email)
        msg['Subject'] = subject

        # Send email
        smtp_server.sendmail(from_email, to_email, msg.as_string())
        smtp_server.quit()

    def post(self, request: HttpRequest, *args, **kwargs):
        """ Handle the form submission. """

        form = ContactForm(request.POST)
        from_email = settings.EMAIL_HOST_USER
        to_email = ['ryan@beyondeventsllc.com', 'info@beyondeventsllc.com']
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            location = form.cleaned_data['location']
            wedding_date = form.cleaned_data['wedding_date']
            comments = form.cleaned_data['comments']
            referred_by = form.cleaned_data['referred_by']

            from_email = 'ryan@beyondeventsllc.com'
            to_email = ['ryan@beyondeventsllc.com']
            subject = f'New Contact from {fname} {lname}'
            message = f'''
                        First Name: {fname} Last Name: {lname}
                        Email: {email}
                        Phone: {phone}
                        Location: {location}
                        Wedding Date: {wedding_date}
                        Comments: {comments}
                        Referred By: {referred_by}'''

            try:
                contact_requests = Contact.objects.create(
                    fname=fname,
                    lname=lname,
                    email=email,
                    phone=phone,
                    location=location,
                    wedding_date=wedding_date,
                    comments=comments,
                    referred_by=referred_by,
                )
                contact_requests.save()

                self.send_custom_email(subject, message, from_email, to_email)

            except Exception as e:
                context = self.get_context_data(**kwargs)
                error_msg = 'There was an error submitting your request.'
                if isinstance(e, IntegrityError):
                    error_msg = 'This email address has already been submitted.'
                form.add_error(None, forms.ValidationError(error_msg))
                context['form'] = form
                return render(request, self.template_name, context)

            return HttpResponseRedirect('/confirm/')
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return render(request, self.template_name, context)


class ConfirmPageView(TemplateView):
    """ Confirmation page view. """

    template_name = "confirm.html"
