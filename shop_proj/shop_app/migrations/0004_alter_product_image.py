# Generated by Django 5.1.3 on 2024-11-11 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_product_category_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.png', upload_to='uploads/'),
        ),
    ]