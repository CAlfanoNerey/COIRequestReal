from django.contrib import admin

# Register your models here.

from .models import UserProfile, User, Requester, Recipient, ContactInfo

admin.site.register(User)
admin.site.register(Recipient)
admin.site.register(Requester)
admin.site.register(ContactInfo)

