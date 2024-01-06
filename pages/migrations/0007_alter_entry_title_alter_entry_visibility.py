# Generated by Django 4.2.3 on 2024-01-03 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_entry_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='visibility',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
