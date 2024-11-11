from django.contrib import admin
from .models import OrAdmin

@admin.register(OrAdmin)
class OrAdminAdmin(admin.ModelAdmin):
    pass

