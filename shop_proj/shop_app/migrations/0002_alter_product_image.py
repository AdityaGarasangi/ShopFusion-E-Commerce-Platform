# Generated by Django 5.1.3 on 2024-11-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='shop_app/media/default.png', upload_to='uploads'),
        ),
    ]
