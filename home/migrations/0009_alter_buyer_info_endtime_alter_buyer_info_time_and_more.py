# Generated by Django 4.1.1 on 2023-01-02 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_contact_alter_buyer_info_endtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer_info',
            name='EndTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 2, 23, 28, 38, 362641), editable=False),
        ),
        migrations.AlterField(
            model_name='buyer_info',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 2, 22, 28, 38, 362641), editable=False),
        ),
        migrations.AlterField(
            model_name='rating',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 2, 22, 28, 38, 362641), editable=False),
        ),
    ]
