import pytest
from django.utils import translation


@pytest.yield_fixture
def activate_en():
    original_language = translation.get_language()
    translation.activate('en')
    yield
    translation.activate(original_language)


@pytest.yield_fixture
def cleared_cache(request):
    from django.core.cache import cache
    cache.clear()
    yield cache
    cache.clear()
