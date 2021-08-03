# Generated by Django 2.0.5 on 2018-08-23 18:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20180824_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='summary_p',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(50)]),
        ),
    ]
