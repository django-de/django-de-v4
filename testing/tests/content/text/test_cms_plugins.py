from unittest import mock

import pytest

from djangode.content.text.cms_plugins import TextPlugin
from djangode.content.text.models import TextContent


@pytest.mark.django_db
class TestTextPlugin:

    def test_context(self):
        plugin = TextPlugin()
        content = TextContent.objects.create(
            headline='Foo',
            text='Baz'
        )

        assert plugin.render({}, content, mock.ANY) == {
            'instance': content,
            'placeholder': mock.ANY,
            'content_id': content.pk,
            'css_class': '',
            'headline': 'Foo',
            'text': 'Baz',
        }
