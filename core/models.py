from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel

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


class ContentPage(Page):
    """
    Standard Article instance
    """
    headline = models.CharField(max_length=255)
    twitter_link = models.CharField(max_length=2048, default="")
    cover = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True
    )
    cover_alt = models.CharField(max_length=1028, default="")
    cover_caption = models.CharField(max_length=255, blank=True)
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
        FieldPanel("headline"),
        ImageChooserPanel("cover"),
        FieldPanel("cover_alt"),
        FieldPanel("cover_caption"),
        FieldPanel("twitter_link"),
        StreamFieldPanel("content"),

    ]

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class ArticlePageImageGallery(Orderable):
    page = ParentalKey(ContentPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class ArticlePage(ContentPage):
    template = "core/article_page.html"
    """
    Multi-part tutorial page
    """
    class Meta:
        verbose_name = "Tutorial"
        verbose_name_plural = "Tutorials"


class FlexPage(Page):
    """
    Generic page - mostly static information
    """
    content = StreamField(
        [
            ("richtext_editor", RichTextBlock()),
            ("code_block", CodeStreamBlock())
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content")
    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
