# Generated by Django 2.1 on 2019-04-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranksaverage',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='rankssingle',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
