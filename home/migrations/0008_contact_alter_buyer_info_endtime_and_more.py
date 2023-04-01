# Generated by Django 4.1.1 on 2023-01-02 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_buyer_info_endtime_alter_buyer_info_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('Details', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='buyer_info',
            name='EndTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 2, 19, 36, 28, 897887), editable=False),
        ),
        migrations.AlterField(
            model_name='buyer_info',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 2, 18, 36, 28, 897887), editable=False),
        ),
        migrations.AlterField(
            model_name='rating',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 2, 18, 36, 28, 897887), editable=False),
        ),
    ]
