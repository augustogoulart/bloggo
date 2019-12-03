from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from .blocks import RichTextBlock


class HomePage(Page):
    """
    Home page model
    """

    # Limits the number of core page instances
    max_count = 1

    banner_title = models.CharField(max_length=256, blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        """
        Adds published live articles to the Home page

        :param request:
        :param args:
        :param kwargs:
        :return: default context plus list of articles
        """
        context = super().get_context(request, *args, **kwargs)
        context['articles'] = ArticlePage.objects.live().public()
        return context

    class Meta:
        verbose_name = "Home Page"


class ArticlePage(Page):
    """
    Standard Article instance
    """

    article_title = models.CharField(max_length=255)
    content = StreamField(
        [
            ("richtext_editor", RichTextBlock())
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("article_title"),
        StreamFieldPanel("content")
    ]

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

