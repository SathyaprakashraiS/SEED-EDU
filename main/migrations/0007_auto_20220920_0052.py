# Generated by Django 3.1.3 on 2022-09-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220919_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(default='Studying...', max_length=250),
        ),
    ]