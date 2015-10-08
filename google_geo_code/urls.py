from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Home:
    url(r'^$', 'apps.home.views.home', name='home'),

    # Order Details
    url(r'^order/(?P<order_id>[\w-]+)/$', 'apps.home.views.details', name='details'),

    # url(r'^google_geo_code/', include('google_geo_code.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
