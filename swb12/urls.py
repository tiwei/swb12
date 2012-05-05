from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('launch.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('social_auth.urls')),
    url(r'^accounts/', include('accounts.urls')),
)
