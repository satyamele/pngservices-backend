# Generated by Django 2.2.5 on 2019-09-26 16:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20190926_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contact',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone: 10 digits allowed.', regex='^\\+?1?\\d{10}$')]),
        ),
    ]
