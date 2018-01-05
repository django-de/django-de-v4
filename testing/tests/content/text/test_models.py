import pytest

from djangode.content.text.models import TextContent


@pytest.mark.django_db
class TestTextContent:

    def test_str(self):
        content = TextContent.objects.create(text='A' * 24)
        assert str(content) == '<{0}>'.format('A' * 23)

    def test_str_headline(self):
        content = TextContent.objects.create(text='Text', headline='Test')
        assert str(content) == '<Test>'
