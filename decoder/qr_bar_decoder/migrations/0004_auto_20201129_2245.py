# Generated by Django 3.1.2 on 2020-11-29 15:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qr_bar_decoder', '0003_auto_20201129_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 15, 45, 54, 38017, tzinfo=utc), verbose_name='Published Date'),
        ),
        migrations.AlterField(
            model_name='list',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 15, 45, 54, 38017, tzinfo=utc), verbose_name='Published Date'),
        ),
    ]