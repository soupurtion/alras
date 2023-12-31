# Generated by Django 4.2.6 on 2023-11-22 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alras_application', '0005_rename_end_time_booking_slot_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='purpose',
        ),
        migrations.AddField(
            model_name='booking',
            name='purpose',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='slot_time',
            field=models.CharField(choices=[('09:00 - 12:00', '09:00 - 12:00'), ('12:00 - 15:00', '12:00 - 15:00'), ('15:00 - 18:00', '15:00 - 18:00')], max_length=20),
        ),
    ]
