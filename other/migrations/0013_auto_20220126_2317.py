# Generated by Django 3.1.3 on 2022-01-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0012_auto_20220126_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinecourses',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
