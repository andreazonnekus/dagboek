# Generated by Django 4.2.3 on 2023-07-23 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inskrywing', '0015_alter_inskrywing_skeppings_tyd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inskrywing',
            name='skeppings_tyd',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 23, 21, 1, 37, 273170)),
        ),
    ]
