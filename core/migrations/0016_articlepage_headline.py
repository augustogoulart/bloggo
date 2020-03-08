# Generated by Django 3.0.4 on 2020-03-08 03:17

import core.blocks
from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_articlepage_cover_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='headline',
            field=wagtail.core.fields.StreamField([('richtext_editor', core.blocks.RichTextBlock())], default=''),
            preserve_default=False,
        ),
    ]