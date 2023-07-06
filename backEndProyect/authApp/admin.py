from django.contrib import admin
from authApp.models.models import *

admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Assistant)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Relative)
admin.site.register(ClinicHistory)
admin.site.register(Diagnostic)
admin.site.register(VitalSigns)
admin.site.register(CareTips)