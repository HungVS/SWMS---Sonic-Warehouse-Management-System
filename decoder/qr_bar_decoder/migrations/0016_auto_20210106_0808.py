# Generated by Django 3.1.2 on 2021-01-06 01:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qr_bar_decoder', '0015_auto_20210106_0802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='name',
        ),
        migrations.AlterField(
            model_name='list',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 6, 1, 8, 35, 984272, tzinfo=utc), verbose_name='Published Date'),
        ),
        migrations.AlterField(
            model_name='section',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 6, 1, 8, 35, 984272, tzinfo=utc), verbose_name='Published Date'),
        ),
    ]
