from django.conf.urls.defaults import *
#from django.contrib.auth.decorators import login_required
from listing.views import *

urlpatterns = patterns('',
    #Listings
    url(r'^$', listings, name='listings'),
        (r'^add/$', 'listing.views.submit_problem'),
        (r'^people/$', 'listing.views.peoplelist'),
                        
                       
)
