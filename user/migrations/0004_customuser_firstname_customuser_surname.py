# Generated by Django 4.2.3 on 2024-02-20 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='firstname',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='customuser',
            name='surname',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
