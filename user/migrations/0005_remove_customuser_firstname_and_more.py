# Generated by Django 4.2.3 on 2024-02-20 12:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_customuser_firstname_customuser_surname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='surname',
        ),
        migrations.AddField(
            model_name='customuser',
            name='birthdate',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='firstname',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='surname',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
