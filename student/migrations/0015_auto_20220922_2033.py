# Generated by Django 3.1.3 on 2022-09-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_compexamresults_writting'),
    ]

    operations = [
        migrations.AddField(
            model_name='compexamresults',
            name='stestname',
            field=models.CharField(default='examname', max_length=200),
        ),
        migrations.AlterField(
            model_name='compexamresults',
            name='stest',
            field=models.CharField(default='testid', max_length=200),
        ),
    ]