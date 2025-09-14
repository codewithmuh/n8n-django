from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import Customer, Ticket


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'full_name', 'site_id')
    search_fields = ('phone_number', 'full_name', 'site_id')
    list_filter = ('site_id',)


@admin.register(Ticket)
class TicketAdmin(GISModelAdmin):
    list_display = (
        'id', 'ticket_uuid', 'reporting_phone', 'ticket_timestamp', 
        'ticket_subject', 'status', 'location_source', 'is_alert_sent'
    )
    list_filter = ('ticket_subject', 'status', 'location_source', 'is_alert_sent', 'is_primary_report')
    search_fields = ('ticket_uuid', 'reporting_phone__phone_number', 'reporting_phone__full_name')
    readonly_fields = ('ticket_uuid', 'ticket_timestamp')
    
    # Map configuration
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 12,
            'default_lat': 40.7128,  # Default to NYC, change as needed
            'default_lon': -74.0060,
        },
    }
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('ticket_uuid', 'reporting_phone', 'ticket_timestamp', 'ticket_subject', 'status')
        }),
        ('Content', {
            'fields': ('original_free_text', 'openai_summary', 'structured_response')
        }),
        ('Location', {
            'fields': ('location_source', 'latitude', 'longitude', 'location'),
            'description': 'The map will automatically update when you enter latitude and longitude values.'
        }),
        ('Flags', {
            'fields': ('is_alert_sent', 'is_primary_report')
        }),
    )