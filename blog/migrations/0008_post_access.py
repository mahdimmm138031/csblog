# Generated by Django 3.1.4 on 2020-12-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201225_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='access',
            field=models.BooleanField(default=False),
        ),
    ]
