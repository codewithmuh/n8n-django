from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_ticket_location'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE VIEW active_tickets AS
            SELECT 
                t.id,
                t.ticket_uuid,
                t.reporting_phone,
                c.full_name as customer_name,
                c.address as customer_address,
                t.ticket_timestamp,
                t.ticket_subject,
                t.status,
                t.location_source,
                t.latitude,
                t.longitude,
                ST_AsText(t.location) as location_wkt,
                t.original_free_text,
                t.openai_summary,
                t.is_alert_sent,
                t.is_primary_report
            FROM tickets t
            LEFT JOIN customers c ON t.reporting_phone = c.phone_number
            WHERE t.status IN ('High Priority', 'Medium Priority')
            AND t.is_primary_report = true
            ORDER BY 
                CASE 
                    WHEN t.status = 'High Priority' THEN 1
                    WHEN t.status = 'Medium Priority' THEN 2
                    ELSE 3
                END,
                t.ticket_timestamp DESC;
            """,
            reverse_sql="DROP VIEW IF EXISTS active_tickets;"
        ),
    ]
