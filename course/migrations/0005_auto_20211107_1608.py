# Generated by Django 3.1.2 on 2021-11-07 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20211107_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='img',
        ),
        migrations.RemoveField(
            model_name='commerce',
            name='img',
        ),
        migrations.RemoveField(
            model_name='engineering',
            name='img',
        ),
        migrations.RemoveField(
            model_name='professional',
            name='img',
        ),
        migrations.RemoveField(
            model_name='science',
            name='img',
        ),
        migrations.AddField(
            model_name='art',
            name='img_url',
            field=models.URLField(default='https://images.hindustantimes.com/rf/image_size_640x362/HT/p2/2015/12/01/Pictures/_c34102da-9849-11e5-b4f4-1b7a09ed2cea.jpg', max_length=300),
        ),
        migrations.AddField(
            model_name='commerce',
            name='img_url',
            field=models.URLField(default='https://images.hindustantimes.com/rf/image_size_640x362/HT/p2/2015/12/01/Pictures/_c34102da-9849-11e5-b4f4-1b7a09ed2cea.jpg', max_length=300),
        ),
        migrations.AddField(
            model_name='engineering',
            name='img_url',
            field=models.URLField(default='https://images.hindustantimes.com/rf/image_size_640x362/HT/p2/2015/12/01/Pictures/_c34102da-9849-11e5-b4f4-1b7a09ed2cea.jpg', max_length=300),
        ),
        migrations.AddField(
            model_name='professional',
            name='img_url',
            field=models.URLField(default='https://images.hindustantimes.com/rf/image_size_640x362/HT/p2/2015/12/01/Pictures/_c34102da-9849-11e5-b4f4-1b7a09ed2cea.jpg', max_length=300),
        ),
        migrations.AddField(
            model_name='science',
            name='img_url',
            field=models.URLField(default='https://images.hindustantimes.com/rf/image_size_640x362/HT/p2/2015/12/01/Pictures/_c34102da-9849-11e5-b4f4-1b7a09ed2cea.jpg', max_length=300),
        ),
    ]
