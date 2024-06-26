# Generated by Django 4.2.11 on 2024-04-28 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('specialization', models.CharField(max_length=200)),
                ('appointment_date', models.CharField(max_length=100)),
                ('available_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_time', models.CharField(max_length=100)),
                ('doctor_name',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outpatient_system.doctor_list')),
            ],
        ),
    ]
