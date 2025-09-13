# Generated manually to add database-level defaults

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_alter_ticket_is_alert_sent_and_more'),
    ]

    operations = [
        migrations.RunSQL(
            # Add database-level defaults
            sql=[
                "ALTER TABLE tickets ALTER COLUMN ticket_uuid SET DEFAULT gen_random_uuid();",
                "ALTER TABLE tickets ALTER COLUMN ticket_timestamp SET DEFAULT NOW();",
                "ALTER TABLE tickets ALTER COLUMN is_alert_sent SET DEFAULT FALSE;",
                "ALTER TABLE tickets ALTER COLUMN is_primary_report SET DEFAULT TRUE;",
            ],
            # Reverse SQL for rollback
            reverse_sql=[
                "ALTER TABLE tickets ALTER COLUMN ticket_uuid DROP DEFAULT;",
                "ALTER TABLE tickets ALTER COLUMN ticket_timestamp DROP DEFAULT;", 
                "ALTER TABLE tickets ALTER COLUMN is_alert_sent DROP DEFAULT;",
                "ALTER TABLE tickets ALTER COLUMN is_primary_report DROP DEFAULT;",
            ]
        ),
    ]