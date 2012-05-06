from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.generic.simple import direct_to_template

#Static Pages in main app
urlpatterns = patterns("",
    url(r"^$", direct_to_template, {"template": "index.html"}, name="home"),
    url(r"^about$", direct_to_template, {"template": "about.html"}, name="about"),
    url(r"^terms/$", direct_to_template, {"template": "terms.html"}, name="terms"),
    url(r"^privacy/$", direct_to_template, {"template": "privacy.html"}, name="privacy"),
    url(r"^dmca/$", direct_to_template, {"template": "dmca.html"}, name="dmca"),
    url(r"^what_next/$", direct_to_template, {"template": "what_next.html"}, name="what_next"),
)

#apps
urlpatterns += patterns('',
    url(r'^launch', include('launch.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('social_auth.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^listing/', include('listing.urls')),
)
