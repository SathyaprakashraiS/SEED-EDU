# Generated by Django 3.1.3 on 2022-09-20 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0016_helpline'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpline',
            name='mail',
            field=models.CharField(default='', max_length=100),
        ),
    ]