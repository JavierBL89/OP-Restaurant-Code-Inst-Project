# Generated by Django 3.2 on 2022-04-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onepico', '0005_rename_time_booking_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='excerpt',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='booking',
            name='prefix',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='surname',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
