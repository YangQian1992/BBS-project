# Generated by Django 2.1 on 2018-08-23 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog01', '0006_auto_20180820_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
