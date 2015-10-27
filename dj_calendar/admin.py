from django.contrib import admin
from dj_calendar.models import CalendarEvent

class CalendarEventAdmin(admin.ModelAdmin):
    class Meta:
        model = CalendarEvent

admin.site.register(CalendarEvent,CalendarEventAdmin)
