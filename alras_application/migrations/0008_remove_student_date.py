# Generated by Django 4.2.6 on 2023-11-22 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alras_application', '0007_day_roomslot_remove_labroom_room_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date',
        ),
    ]
