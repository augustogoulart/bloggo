from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from .blocks import RichTextBlock, CodeStreamBlock


class HomePage(Page):

    max_count = 1   # Limits the number of core page instances

    def get_context(self, request, *args, **kwargs):
        """
        Adds published live articles to the Home page

        :return: default context plus list of articles
        """
        context = super().get_context(request, *args, **kwargs)
        context['articles'] = ArticlePage.objects.live().public().filter(is_article=True)
        return context

    class Meta:
        verbose_name = "Home Page"


class ArticlePage(Page):
    """
    Standard Article instance
    """

    article_title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_article = models.BooleanField(default=True)

    content = StreamField(
        [
            ("richtext_editor", RichTextBlock()),
            ("code_block", CodeStreamBlock())
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("article_title"),
        FieldPanel("is_article"),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class FlexPage(Page):
    """
    Generic page - mostly static information
    """
    page_title = models.CharField(max_length=255)

    content = StreamField(
        [
            ("richtext_editor", RichTextBlock()),
            ("code_block", CodeStreamBlock())
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
        StreamFieldPanel("content")
    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
