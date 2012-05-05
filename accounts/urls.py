from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
    url(r'^profile/$', 'profile_view', name='accounts_profile'),
)
