# Generated by Django 5.1.3 on 2024-11-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0005_order_cart_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]