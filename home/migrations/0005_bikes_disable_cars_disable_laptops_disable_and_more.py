# Generated by Django 4.1.1 on 2023-01-01 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_buyer_info_varification_alter_buyer_info_endtime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cars',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='laptops',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mobiles',
            name='disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='buyer_info',
            name='EndTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 2, 0, 19, 24, 466052), editable=False),
        ),
        migrations.AlterField(
            model_name='buyer_info',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 1, 23, 19, 24, 466052), editable=False),
        ),
        migrations.AlterField(
            model_name='rating',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 1, 23, 19, 24, 466052), editable=False),
        ),
    ]
