# Generated by Django 4.2.3 on 2024-01-09 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_entry_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='user',
            new_name='author',
        ),
    ]
