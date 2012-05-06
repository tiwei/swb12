from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
    url(r'^profile/$', 'profile_view', name='accounts_profile'),
    url(r'^profile/(?P<profile_id>\d+)/$', 'profile_show_view', name='accounts_profile_show'),
)
