import uuid
from django.db import models
from django.utils import timezone
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point


class Customer(models.Model):
    phone_number = models.CharField(max_length=20, primary_key=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    site_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.phone_number})"

    class Meta:
        db_table = 'customers'


class Ticket(models.Model):
    TICKET_SUBJECT_CHOICES = [
        ('self_location', 'Self Location'),
        ('registered_address', 'Registered Address'),
    ]
    
    STATUS_CHOICES = [
        ('High Priority', 'High Priority'),
        ('Medium Priority', 'Medium Priority'),
        ('Info', 'Info'),
    ]
    
    LOCATION_SOURCE_CHOICES = [
        ('shared_location', 'Shared Location'),
        ('from_customers_table', 'From Customers Table'),
    ]

    id = models.AutoField(primary_key=True)
    ticket_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    reporting_phone = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE, 
        to_field='phone_number',
        db_column='reporting_phone',
        blank=True, null=True
    )
    ticket_timestamp = models.DateTimeField(auto_now_add=True)
    ticket_subject = models.CharField(max_length=50, blank=True, null=True)
    structured_response = models.JSONField(blank=True, null=True)
    original_free_text = models.TextField(blank=True, null=True)
    openai_summary = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True, null=True)
    location_source = models.CharField(max_length=20, choices=LOCATION_SOURCE_CHOICES, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    location = gis_models.PointField(blank=True, null=True, srid=4326)
    is_alert_sent = models.BooleanField(default=False)
    is_primary_report = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Auto-create Point field from latitude/longitude
        if self.latitude and self.longitude:
            self.location = Point(float(self.longitude), float(self.latitude))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket {self.id} - {self.ticket_subject} ({self.status})"

    class Meta:
        db_table = 'tickets'