import models

from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(models.Event, EventAdmin)