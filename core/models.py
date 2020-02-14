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
        context['articles'] = ArticlePage.objects.live().public()
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


class TutorialPage(ArticlePage):
    """
    Multi-part tutorial page
    """
    class Meta:
        verbose_name = "Tutorial"
        verbose_name_plural = "Tutorials"


class TutorialPageList(Page):
    max_count = 1  # Limits the number of core page instances

    def get_context(self, request, *args, **kwargs):
        """
        Lists published live tutorials

        :return: default context plus list of tutorials
        """
        context = super().get_context(request, *args, **kwargs)
        context['tutorials'] = TutorialPage.objects.live().public()
        return context

    class Meta:
        verbose_name = "Tutorials List"


class StoryPage(ArticlePage):
    """
    Single story page
    """
    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"


class StoryPageList(Page):
    max_count = 1  # Limits the number of core page instances

    def get_context(self, request, *args, **kwargs):
        """
        Lists published live stories

        :return: default context plus list of stories
        """
        context = super().get_context(request, *args, **kwargs)
        context['stories'] = StoryPage.objects.live().public()
        return context

    class Meta:
        verbose_name = "Stories List"
