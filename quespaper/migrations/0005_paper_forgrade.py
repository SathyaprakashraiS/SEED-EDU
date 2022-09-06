# Generated by Django 3.1.3 on 2021-10-04 09:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quespaper', '0004_delete_mockpm'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='forgrade',
            field=models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(10)]),
        ),
    ]
