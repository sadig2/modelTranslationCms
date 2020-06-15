"""Steamfields live in here"""
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True,help_text="Add your title")
    text= blocks.TextBlock(required=True,help_text="Add additional text")


    class Meta: #noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    """Cards with images and text and buttons"""
    title = blocks.CharBlock(required=True,help_text="Add your title")
    
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ("image", ImageChooserBlock(required=True)),
            ("title", blocks.CharBlock(required=True,max_length=40)),
            ("text", blocks.TextBlock(required=True,max_length=200)),
            ("button",blocks.PageChooserBlock(required=False)),
            ("button_url",blocks.URLBlock(required=False, help_text="if the button page above is used then it ll be used")),
        ])
    )

    class Meta:
        template = "streams/card_block.html"
        icon="plcaholder"
        label="staff Cards"


class RichTextBlock(blocks.RichTextBlock):
    """rich text with all the features"""

    class Meta: #noqa
        template= "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichTextBlock(blocks.RichTextBlock):
    """rich text with all the features"""

    class Meta: #noqa
        template= "streams/richtext_block.html"
        icon = "edit"
        label = "Simpl RichText"

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link"
        ]
   
class CTABlock(blocks.StructBlock):
    """A simple call to action section"""

    title= blocks.CharBlock(required=False,max_length=50)
    text = blocks.RichTextBlock(required=True, features=["bold","italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url=blocks.URLBlock(required=False)
    button_text=blocks.CharBlock(required=True,default="Learn more",max_length=100)

    class Meta: # noqa
        template = "streams/cta_block.html"
        icon="placeholder"
        label="Call to Action"



class LinkStructValue(blocks.StructValue):
    """additional logic for our url"""

    def url(self):
        button_page  = self.get("button_page")
        button_url  = self.get("button_url")

        if button_page:
            return button_page.url
        elif button_url:
            return button_url

        return None




class ButtonBlock(blocks.StructBlock):
    """An external or internal url"""
    button_page = blocks.PageChooserBlock(required=False)
    button_url=blocks.URLBlock(required=False)


    class Meta: # noqa
        template = "streams/button_block.html"
        icon="placeholder"
        label="Single button"
        value_class =LinkStructValue
