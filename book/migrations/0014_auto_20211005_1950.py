# Generated by Django 3.1.3 on 2021-10-05 14:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_books_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktypes',
            name='forgrade',
            field=models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(10)]),
        ),
    ]
