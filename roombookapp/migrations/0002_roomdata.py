# Generated by Django 4.1.4 on 2022-12-30 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roombookapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='roomdata',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=100)),
            ],
        ),
    ]
