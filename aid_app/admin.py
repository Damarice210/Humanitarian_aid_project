from django.contrib import admin
from .models import Beneficiary, AidItem, Distribution

admin.site.register(Beneficiary)
admin.site.register(AidItem)
admin.site.register(Distribution)
