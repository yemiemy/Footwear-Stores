# Generated by Django 2.2.2 on 2019-07-20 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=29.99, max_digits=100)),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'unique_together': {('title', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=True)),
                ('image', models.ImageField(upload_to='products/images/')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('featured', models.BooleanField(default=False)),
                ('male', models.BooleanField(default=False)),
                ('female', models.BooleanField(default=False)),
                ('casual', models.BooleanField(default=False)),
                ('sport', models.BooleanField(default=False)),
                ('formal', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('nike', models.BooleanField(default=False)),
                ('adidas', models.BooleanField(default=False)),
                ('givenchy', models.BooleanField(default=False)),
                ('gucci', models.BooleanField(default=False)),
                ('slip_ons', models.BooleanField(default=False)),
                ('boots', models.BooleanField(default=False)),
                ('sandals', models.BooleanField(default=False)),
                ('lace_ups', models.BooleanField(default=False)),
                ('oxfords', models.BooleanField(default=False)),
                ('black', models.BooleanField(default=False)),
                ('white', models.BooleanField(default=False)),
                ('blue', models.BooleanField(default=False)),
                ('red', models.BooleanField(default=False)),
                ('green', models.BooleanField(default=False)),
                ('grey', models.BooleanField(default=False)),
                ('orange', models.BooleanField(default=False)),
                ('brown', models.BooleanField(default=False)),
                ('leather', models.BooleanField(default=False)),
                ('suede', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('size', 'size'), ('color', 'color'), ('package', 'package')], default='size', max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductImage')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]