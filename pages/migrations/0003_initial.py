# Generated by Django 4.2.3 on 2024-01-02 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0002_delete_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField()),
                ('visibility', models.BooleanField(default=True)),
                ('category', models.CharField(blank=True, choices=[('general', 'General'), ('news', 'News'), ('events', 'Events')], max_length=50, null=True)),
                ('language', models.CharField(blank=True, choices=[('af', 'Afrikaans'), ('en', 'English'), ('ja', 'Japanese'), ('zh', 'Chinese')], max_length=2, null=True)),
                ('entry_date', models.DateField(blank=True, default=datetime.datetime(2024, 1, 2, 21, 38, 32, 583707))),
            ],
        ),
    ]