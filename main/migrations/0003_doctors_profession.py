# Generated by Django 5.0.3 on 2024-03-06 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_remove_appointments_mail_or_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='profession',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
