# Generated by Django 2.1.5 on 2019-04-25 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_post_internship'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='website',
            field=models.CharField(default='', max_length=30),
        ),
    ]
