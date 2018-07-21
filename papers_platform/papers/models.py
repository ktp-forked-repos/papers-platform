from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class PaperPage(Page):
    link = models.URLField()
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('link'),
        FieldPanel('intro', classname="full"),
    ]
