# Generated by Django 3.1.4 on 2020-12-25 09:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=datetime.datetime(2020, 12, 25, 9, 19, 18, 635399, tzinfo=utc), height_field=400, max_length=50, upload_to='uploads/% Y/% m/% d/', width_field=400),
            preserve_default=False,
        ),
    ]
