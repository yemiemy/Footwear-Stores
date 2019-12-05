# Generated by Django 2.2.2 on 2019-07-21 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190721_0028'),
        ('carts', '0004_cartitem_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='coupon',
        ),
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Coupon'),
        ),
    ]