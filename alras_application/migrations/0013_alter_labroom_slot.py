# Generated by Django 4.2.6 on 2023-11-22 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alras_application', '0012_alter_student_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labroom',
            name='slot',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='alras_application.roomslot'),
        ),
    ]
