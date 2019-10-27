from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    """
    Home page model
    """

    # Limits the number of core page instances
    max_count = 1

    banner_title = models.CharField(max_length=256, blank=False, null=True)
    banner_subtitle = RichTextField(features=['bold', 'italic'])

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
    ]

    class Meta:
        verbose_name = "Home Page"