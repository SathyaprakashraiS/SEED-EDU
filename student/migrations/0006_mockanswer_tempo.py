# Generated by Django 3.1.3 on 2021-09-26 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_mockanswer_evaluated'),
    ]

    operations = [
        migrations.AddField(
            model_name='mockanswer',
            name='tempo',
            field=models.IntegerField(default=1),
        ),
    ]
