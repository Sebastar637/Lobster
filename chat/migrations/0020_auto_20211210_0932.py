# Generated by Django 3.1.7 on 2021-12-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0019_auto_20211210_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='room',
            field=models.IntegerField(null=True),
        ),
    ]
