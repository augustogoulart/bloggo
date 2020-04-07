from wagtail.tests.utils import WagtailPageTests
from ..models import ArticlePage, ContentPage


class TestStoryPage(WagtailPageTests):
    def test_can_create_a_page(self):
        self.assertCanCreateAt(ArticlePage, ContentPage)
