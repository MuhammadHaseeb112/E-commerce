# Generated by Django 4.1.1 on 2022-12-29 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer_info',
            name='EndTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 29, 22, 29, 11, 803192), editable=False),
        ),
        migrations.AlterField(
            model_name='buyer_info',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 29, 21, 29, 11, 803192), editable=False),
        ),
        migrations.AlterField(
            model_name='rating',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 29, 21, 29, 11, 803192), editable=False),
        ),
    ]