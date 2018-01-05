from unittest import mock

from djangode.content.base import BasePlugin


class DummyPlugin(BasePlugin):
    base_fields = ('field1', 'field2', 'field3', 'field4')


class DummyPluginWithAdvancedFields(BasePlugin):
    base_fields = ('field1', 'field2')
    advanced_fields = ('field3', 'field4')
    context_fields = ('field1',)


class TestBasePlugin:

    def test_get_fieldsets_base_fields(self, rf, activate_en):
        plugin = DummyPlugin()
        request = rf.get('/')

        expected_fieldset = [(
            None, {
                'fields': ('field1', 'field2', 'field3', 'field4')
            },
        ), (
            'Advanced options', {
                'classes': ('collapse',), 'fields': ('css_class',)
            }
        )]

        assert plugin.get_fieldsets(request) == expected_fieldset

    def test_get_fieldsets_with_advanced_fieldset(self, rf, activate_en):
        plugin = DummyPluginWithAdvancedFields()
        request = rf.get('/')

        expected_fieldset = [
            (None, {
                'fields': ('field1', 'field2')
            }),
            ('Advanced options', {
                'fields': ('field3', 'field4'), 'classes': ('collapse',)
            })
        ]
        assert plugin.get_fieldsets(request) == expected_fieldset

    def test_render_minimal(self):
        plugin = DummyPlugin()

        instance_mock = mock.Mock()
        instance_mock.pk = 1
        instance_mock.anchor = ''
        instance_mock.css_class = ''

        assert plugin.render({}, instance_mock, mock.ANY) == {
            'instance': instance_mock,
            'placeholder': mock.ANY,
            'content_id': 1,
            'css_class': '',
        }

    def test_render_with_context_fields(self):
        plugin = DummyPluginWithAdvancedFields()

        instance_mock = mock.Mock()
        instance_mock.pk = 2
        instance_mock.css_class = 'tested'
        instance_mock.field1 = 'mocked'

        assert plugin.render({}, instance_mock, mock.ANY) == {
            'instance': instance_mock,
            'placeholder': mock.ANY,
            'content_id': 2,
            'field1': 'mocked'
        }
