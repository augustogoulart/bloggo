# Generated by Django 3.0.4 on 2020-04-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_articlepage_twitter_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='cover_alt',
            field=models.CharField(default='', max_length=1028),
        ),
    ]
