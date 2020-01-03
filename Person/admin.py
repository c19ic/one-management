from django.contrib import admin

from .models import PersonSizes, PersonGender, PersonInformation


admin.site.register(PersonSizes)
admin.site.register(PersonGender)
admin.site.register(PersonInformation)