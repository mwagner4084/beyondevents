from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms


class ContactForm(forms.Form):
    """ Form for the contact page. """

    fname = forms.CharField(
        help_text='',
        label='First Name',
        max_length=200,
        widget=forms.TextInput()
    )
    lname = forms.CharField(
        help_text='',
        label='Last Name',
        max_length=200,
        widget=forms.TextInput()
    )
    email = forms.EmailField(
        help_text='',
        label='Email Address',
        max_length=200,
        widget=forms.EmailInput()
    )
    phone = forms.CharField(
        help_text='',
        label='Phone Number',
        max_length=200,
        widget=forms.TextInput()
    )
    location = forms.CharField(
        help_text='',
        label='Location',
        max_length=200,
        widget=forms.TextInput()
    )
    wedding_date = forms.DateField(
        help_text='',
        label='Wedding Date (MM/DD/YYYY)',
        widget=forms.DateInput()
    )
    comments = forms.CharField(
        help_text='',
        label='Comments',
        max_length=500,
        widget=forms.TextInput()
    )
    referred_by = forms.CharField(
        help_text='',
        label='How did you hear about us?',
        max_length=200,
        widget=forms.TextInput()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-contactForm'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            FloatingField('fname'),
            FloatingField('lname'),
            FloatingField('email'),
            FloatingField('phone'),
            FloatingField('location'),
            FloatingField('wedding_date'),
            FloatingField('comments'),
            FloatingField('referred_by'),
            Submit('submit', 'Submit')
        )

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Contact Us'
    #     return context
