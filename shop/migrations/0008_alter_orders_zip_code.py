# Generated by Django 3.2.8 on 2021-10-15 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_orders_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.IntegerField(default='', max_length=5),
        ),
    ]
