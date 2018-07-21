from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class PaperPage(Page):
    link = models.URLField()
    video_id = models.CharField(max_length=32)
    summary = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('link'),
        FieldPanel('video_id'),
        FieldPanel('summary', classname="full"),
    ]
