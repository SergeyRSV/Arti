from django.contrib import admin
from .models import CustomUsers, CustomSettingsScheduler


class CAdminPanel(admin.ModelAdmin):
    pass


admin.site.register(CustomUsers, CAdminPanel)
admin.site.register(CustomSettingsScheduler, CAdminPanel)
