# Generated by Django 3.2 on 2022-05-22 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onepico', '0021_auto_20220522_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='people',
            field=models.BigIntegerField(null=True),
        ),
    ]
