from django.conf.urls import patterns, url
from django.contrib.auth.views import logout

urlpatterns = patterns('accounts.views',
    url(r'^profile/$', 'profile_view', name='accounts_profile'),
    url(r'^profile/(?P<profile_id>\d+)/$', 'profile_show_view', name='accounts_profile_show'),
    url(r'^logout/$', logout, name='logout'),
)
