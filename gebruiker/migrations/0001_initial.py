# Generated by Django 4.2.3 on 2023-07-23 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gebruiker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gebruikersNaam', models.CharField(max_length=80)),
            ],
        ),
    ]
