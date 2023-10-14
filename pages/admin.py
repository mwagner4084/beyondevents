from django.contrib import admin

# from .forms import ContactForm
from .models import Contact

# class ContactAdmin(admin.ModelAdmin):
#     form = ContactForm
#     model = Contact

#     list_display = ('fname', 'lname', 'email', 'phone', 'location', 'wedding_date',
#                     'comments', 'referred_by', 'date_added', 'contacted', 'notes')
#     list_filter = ('contacted', 'date_added', 'wedding_date')
#     search_fields = ('fname', 'lname', 'email', 'phone', 'location',
#                      'wedding_date', 'comments', 'referred_by', 'notes')
#     ordering = ('-date_added',)


admin.site.register(Contact)
