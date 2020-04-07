from datetime import datetime

import pytest
from django.utils import timezone

from ..models import ArticlePage


@pytest.mark.django_db()
def test_create_at():
    article_page = ArticlePage(created_at=timezone.now())
    assert type(article_page.created_at) is datetime


@pytest.mark.django_db()
def test_create_at():
    article_page = ArticlePage(updated_at=timezone.now())
    assert type(article_page.updated_at) is datetime


@pytest.mark.django_db()
def test_article_can_have_a_cover_picture():
    assert ArticlePage.cover


@pytest.mark.django_db()
def test_article_has_a_cover_caption():
    article_page_cover_caption = ArticlePage(cover_caption="Nice cover caption")
    assert article_page_cover_caption.cover_caption

