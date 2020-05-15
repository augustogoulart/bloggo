import pytest


@pytest.mark.django_db()
def test_page_has_social_links(client):
    social_links = [
        b'https://www.instagram.com/augusto_goulartc/',
        b'https://github.com/augustogoulart',
        b'https://twitter.com/gus_goulart',
        b'https://t.me/augustogoulart',
        b'https://www.linkedin.com/in/augustogoulart/'
    ]

    resp = client.get('/')
    assert False not in [social_link in resp.content for social_link in social_links]
