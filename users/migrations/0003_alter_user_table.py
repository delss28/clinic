# Generated by Django 4.2.7 on 2024-05-15 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_dateofbirth_user_number'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
