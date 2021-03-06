# Generated by Django 3.2 on 2022-05-06 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onepico', '0018_auto_20220506_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('slug', models.SlugField(null=True)),
                ('surname', models.CharField(blank=True, max_length=30)),
                ('people', models.BigIntegerField()),
                ('prefix', models.BigIntegerField()),
                ('phone', models.BigIntegerField()),
                ('date', models.DateField(verbose_name='%Y-%m-%d')),
                ('start_time', models.TimeField(verbose_name='%H:%M')),
                ('opening_time', models.TimeField(verbose_name='%H:%M')),
                ('closing_time', models.TimeField(verbose_name='%H:%M')),
                ('email', models.EmailField(max_length=100)),
                ('excerpt', models.CharField(blank=True, max_length=500, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('slug', models.SlugField(null=True)),
                ('surname', models.CharField(blank=True, max_length=30)),
                ('people', models.BigIntegerField()),
                ('prefix', models.BigIntegerField()),
                ('phone', models.BigIntegerField()),
                ('date', models.DateField(verbose_name='%Y-%m-%d')),
                ('start_time', models.TimeField(verbose_name='%H:%M')),
                ('opening_time', models.TimeField(verbose_name='%H:%M')),
                ('closing_time', models.TimeField(verbose_name='%H:%M')),
                ('email', models.EmailField(max_length=100)),
                ('excerpt', models.CharField(blank=True, max_length=500, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tablelunch',
            name='table_id',
        ),
        migrations.DeleteModel(
            name='TableDinner',
        ),
        migrations.DeleteModel(
            name='TableLunch',
        ),
    ]
