# Generated by Django 2.2.28 on 2022-05-01 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220501_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='person_name',
            field=models.CharField(max_length=150),
        ),
    ]
