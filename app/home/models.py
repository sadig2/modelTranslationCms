from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from streams import blocks
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True, default="")


    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL)


    content = StreamField(
        [
        ("title_and_text",blocks.TitleAndTextBlock()),

        ],
        null=True,
        blank= True,

    )

    content_panels = Page.content_panels + [

        MultiFieldPanel([
            ImageChooserPanel('image')
        ],heading= " Common Fields"),

        MultiFieldPanel([
        FieldPanel('body'),
        StreamFieldPanel('content'),
        ],heading="Translatable fields")

      
    ]