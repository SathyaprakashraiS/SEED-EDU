# Generated by Django 3.1.3 on 2021-08-24 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profpic',
            field=models.ImageField(default='images/profpic.jpeg', upload_to='images'),
        ),
    ]
