# Generated by Django 2.0.dev20170705064109 on 2017-08-11 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20170811_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(),
        ),
    ]
