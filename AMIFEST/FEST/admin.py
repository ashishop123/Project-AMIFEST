from django.contrib import admin
from FEST.models import event
from FEST.models import user_registration
# Register your models here.

admin.site.register(event)

admin.site.register(user_registration)
