# Generated by Django 3.0.7 on 2020-06-15 08:47

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='content_az',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='content_en',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='content_ru',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True))]))], blank=True, null=True),
        ),
    ]
