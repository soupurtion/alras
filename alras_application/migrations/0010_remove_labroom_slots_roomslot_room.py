# Generated by Django 4.2.6 on 2023-11-22 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alras_application', '0009_student_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labroom',
            name='slots',
        ),
        migrations.AddField(
            model_name='roomslot',
            name='room',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='alras_application.labroom'),
        ),
    ]
