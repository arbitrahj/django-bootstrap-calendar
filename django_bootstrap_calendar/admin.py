from django.contrib import admin
from django_bootstrap_calendar.models import CalendarEvent

class CalendarEventAdmin(admin.ModelAdmin):
    class Meta:
        model = CalendarEvent

admin.site.register(CalendarEvent,CalendarEventAdmin)
