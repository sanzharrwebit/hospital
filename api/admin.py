from django.contrib import admin

# Register your models here.
from .models import Doctor, Visit, Patient, Service, Specialization

admin.site.register(Doctor)
admin.site.register(Visit)
admin.site.register(Patient)
admin.site.register(Service)
admin.site.register(Specialization)
