# Generated by Django 3.0.7 on 2020-06-15 08:28

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_az',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_en',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_ru',
            field=wagtail.core.fields.RichTextField(blank=True, default='', null=True),
        ),
    ]
