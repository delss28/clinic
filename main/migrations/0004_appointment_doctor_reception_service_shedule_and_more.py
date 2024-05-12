# Generated by Django 5.0.3 on 2024-04-24 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_doctors_profession'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('ENT', 'ЛОР'), ('Surgery', 'Хирургия'), ('Gynecology', 'Гинекология'), ('Allergology-immunology', 'Аллерго-иммунология'), ('Dentistry', 'Стоматология'), ('Ophthalmology', 'Офтальмология'), ('Infectious_disease_specialist', 'Инфекционист'), ('Gastroentorology', 'Гастроэнторология'), ('Ultrasound_diagnostics', 'УЗИ диагностика'), ('Cardiology', 'Кардиология'), ('Endocrinology', 'Эндокринология'), ('Physiotherapy', 'Физиотерапия'), ('Psychiatry', 'Психиатрия'), ('Geneticist', 'Генетик'), ('Dermatology', 'Дерматология'), ('Neurology', 'Неврология'), ('Endoscopy', 'Эндоскопия'), ('Traumalogy-ortopedics', 'Травматология-ортопедия')], default='ЛОР', max_length=55)),
                ('dateTimeService', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('Job_title', models.CharField(max_length=50)),
                ('work_experience', models.IntegerField()),
                ('phone', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=254)),
                ('room_number', models.IntegerField()),
                ('Salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('field_of_medicine', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_doctors', to='main.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Shedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reception_day', models.DateField()),
                ('Reception_hours', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sick_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaints', models.CharField(max_length=50)),
                ('end_date_of_treatment', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Appointments',
        ),
        migrations.RemoveField(
            model_name='services',
            name='doctor',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='first_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fname_user', to='main.user'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='last_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lname_user', to='main.user'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='mail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mail_user', to='main.user'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='number_user', to='main.user'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patronymic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patronymic_user', to='main.user'),
        ),
        migrations.AddField(
            model_name='reception',
            name='id_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_users', to='main.user'),
        ),
        migrations.AddField(
            model_name='reception',
            name='id_service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_services', to='main.service'),
        ),
        migrations.AddField(
            model_name='reception',
            name='id_shedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_shedul', to='main.shedule'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Shedule_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_shedules', to='main.shedule'),
        ),
        migrations.AddField(
            model_name='user',
            name='id_sick_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='id_sick_lists', to='main.sick_list'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Doctors',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]
