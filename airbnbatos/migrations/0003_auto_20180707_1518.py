# Generated by Django 2.0.6 on 2018-07-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbnbatos', '0002_auto_20180707_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvexport',
            name='reviews',
            field=models.IntegerField(),
        ),
    ]