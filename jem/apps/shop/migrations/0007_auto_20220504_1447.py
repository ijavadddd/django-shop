# Generated by Django 3.2.5 on 2022-05-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_coverimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default=None, upload_to='images/products'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='main_img',
            field=models.ImageField(upload_to='images/products'),
        ),
    ]
