from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField


class HomePage(Page):
    body = RichTextField(blank=True, default="")

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]