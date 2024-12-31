# Generated by Django 3.1.6 on 2024-12-31 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubwayLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('status', models.CharField(choices=[('normal', 'Normal'), ('delayed', 'Delayed')], default='normal', max_length=10)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('total_delay_duration', models.DurationField(default=datetime.timedelta(0))),
                ('delay_start_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
