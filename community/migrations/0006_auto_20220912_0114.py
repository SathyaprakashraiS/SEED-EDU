# Generated by Django 3.1.3 on 2022-09-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_community_commicon'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='visibility',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='community',
            name='visibility',
            field=models.BooleanField(default=True),
        ),
    ]
