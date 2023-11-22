# Generated by Django 4.2.6 on 2023-11-22 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alras_application', '0003_rename_room_labroom_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.CharField(choices=[('09:00', '09:00 - 12:00'), ('12:00', '12:00 - 15:00'), ('15:00', '15:00 - 18:00')], max_length=5)),
                ('end_time', models.CharField(choices=[('09:00', '09:00 - 12:00'), ('12:00', '12:00 - 15:00'), ('15:00', '15:00 - 18:00')], max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='labroom',
            name='slots',
        ),
        migrations.RemoveField(
            model_name='labroom',
            name='title',
        ),
        migrations.RemoveField(
            model_name='student',
            name='slot',
        ),
        migrations.AddField(
            model_name='labroom',
            name='room_number',
            field=models.CharField(blank=True, choices=[('101-A', 'Room 101-A'), ('102-A', 'Room 102-A'), ('103-B', 'Room 103-B'), ('104-B', 'Room 104-B'), ('105-C', 'Room 105-C')], max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='purpose',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='RoomSlot',
        ),
        migrations.AddField(
            model_name='booking',
            name='lab_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alras_application.labroom'),
        ),
        migrations.AddField(
            model_name='booking',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]