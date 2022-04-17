# Generated by Django 3.2.5 on 2022-04-17 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
