from django.conf.urls import patterns, url

urlpatterns = patterns('launch.views',
    url(r'^$', 'index_view', name='launch_index'),
)
