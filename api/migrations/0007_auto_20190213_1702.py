# Generated by Django 2.1.1 on 2019-02-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190211_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='relevent_file',
            field=models.FileField(default=False, upload_to=''),
        ),
    ]
