# Generated by Django 4.1.4 on 2022-12-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookingdata',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=100, null=True)),
                ('room_go', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('book_detail', models.CharField(max_length=100, null=True)),
                ('book_user', models.CharField(max_length=100)),
                ('book_tel', models.CharField(max_length=12)),
            ],
        ),
    ]