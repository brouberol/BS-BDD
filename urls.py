from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Admin urls
urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# Default and common urls
urlpatterns += patterns('',
                        )

# App-level urls
urlpatterns += patterns('',
    url(r'^stage/', include('stage.urls')),
    url(r'^upload/', include('upload.urls')),
)
