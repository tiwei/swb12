from django.conf.urls.defaults import *
#from django.contrib.auth.decorators import login_required
from listing.views import listings


urlpatterns = patterns('',
    #Listings
    url(r'^$', listings,
        name='listings'),
                       
)
