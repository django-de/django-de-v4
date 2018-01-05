from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.static import serve


urlpatterns = []


if settings.DEBUG:
    urlpatterns += [
        url(
            r'^%s(?P<path>.*)$' % settings.MEDIA_URL.strip('/'),
            serve, {'document_root': settings.MEDIA_ROOT}
        ),
    ]


urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cms': CMSSitemap}}, name='sitemap-xml'),
    url(r'', include('cms.urls')),
]
