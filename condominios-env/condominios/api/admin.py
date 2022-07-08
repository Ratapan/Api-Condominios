from django.contrib import admin
from .models import Condominium,House,Resident,Residence

# Register your models here.

admin.site.register(Condominium)
admin.site.register(House)
admin.site.register(Resident)
admin.site.register(Residence)