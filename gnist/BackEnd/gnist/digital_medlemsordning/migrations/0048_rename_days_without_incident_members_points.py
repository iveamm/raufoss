# Generated by Django 5.0.1 on 2024-05-12 21:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("digital_medlemsordning", "0047_remove_members_certificate"),
    ]

    operations = [
        migrations.RenameField(
            model_name="members",
            old_name="days_without_incident",
            new_name="points",
        ),
    ]
