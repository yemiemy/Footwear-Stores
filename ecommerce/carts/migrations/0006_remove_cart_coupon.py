# Generated by Django 2.2.2 on 2019-07-21 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20190721_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='coupon',
        ),
    ]
