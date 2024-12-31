from django.contrib import admin
from wingman.models import WingmanSettings


@admin.register(WingmanSettings)
class WingmanSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'cache_expiry', 'description')
    search_fields = ('name', 'description')
    list_filter = ('value',)
