# Generated by Django 4.2.7 on 2024-05-21 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_appointment_reception_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='reception_date',
            new_name='appointment_date',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='reception_time',
            new_name='appointment_time',
        ),
    ]