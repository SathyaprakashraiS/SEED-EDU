# Generated by Django 3.1.3 on 2022-09-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220920_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='contactnumber',
            field=models.CharField(default='9876543210', max_length=13),
        ),
    ]
