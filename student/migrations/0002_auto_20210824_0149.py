# Generated by Django 3.1.3 on 2021-08-23 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QAnswersheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(default='studentname', max_length=200)),
                ('semail', models.CharField(default='studentemail', max_length=200)),
                ('sgrade', models.CharField(default='studentgrade', max_length=200)),
                ('stest', models.CharField(default='testname', max_length=200)),
                ('spoint', models.CharField(default='marksobtained', max_length=200)),
                ('sremark', models.CharField(default='remark', max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Answersheet',
        ),
    ]
