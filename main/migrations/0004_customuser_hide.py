# Generated by Django 3.1.3 on 2021-08-25 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210825_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='hide',
            field=models.BooleanField(default=False),
        ),
    ]
