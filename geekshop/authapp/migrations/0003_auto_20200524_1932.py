# Generated by Django 3.0.6 on 2020-05-24 14:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20200524_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 26, 14, 32, 44, 908541, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
