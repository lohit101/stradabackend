# Generated by Django 3.2.20 on 2023-09-03 19:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stradaapp', '0009_auto_20230904_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50, verbose_name='First Name')),
                ('lname', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('message', models.CharField(max_length=250, verbose_name='Message')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=models.CharField(default=uuid.UUID('f9a1f752-5873-4be2-81c1-c56449ea53f0'), max_length=40, primary_key=True, serialize=False, verbose_name='Product ID'),
        ),
    ]
