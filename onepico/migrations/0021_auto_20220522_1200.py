# Generated by Django 3.2 on 2022-05-22 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onepico', '0020_auto_20220506_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='surname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
