# Generated by Django 2.2.5 on 2019-09-26 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_customer_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='price',
            new_name='investment',
        ),
    ]
