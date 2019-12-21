import pytest
from ..models import ArticlePage
from django.utils import timezone
from datetime import datetime


@pytest.mark.django_db()
def test_create_at():
    article_page = ArticlePage(created_at=timezone.now())
    assert type(article_page.created_at) is datetime
