# Generated by Django 3.2.20 on 2023-09-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stradaapp', '0004_alter_product_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=models.UUIDField(primary_key=True, serialize=False, verbose_name='Product ID'),
        ),
    ]
