# Generated by Django 3.1.3 on 2022-09-11 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20220911_2325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={},
        ),
        migrations.AlterField(
            model_name='chat',
            name='communitytype',
            field=models.IntegerField(default=0),
        ),
    ]