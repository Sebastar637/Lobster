# Generated by Django 3.1.7 on 2021-12-01 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20211201_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.CharField(max_length=255),
        ),
    ]
