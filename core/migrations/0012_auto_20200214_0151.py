# Generated by Django 3.0.3 on 2020-02-14 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('core', '0011_flexpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialPage',
            fields=[
                ('articlepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.ArticlePage')),
            ],
            options={
                'verbose_name': 'Tutorial',
                'verbose_name_plural': 'Tutorials',
            },
            bases=('core.articlepage',),
        ),
        migrations.CreateModel(
            name='TutorialPageList',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Tutorials List',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='articlepage',
            name='is_article',
        ),
    ]
