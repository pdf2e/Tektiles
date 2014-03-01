from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blogadmin/', include(admin.site.urls)),
    url(r'^', include('frontend.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^webstore/', include('webstore.urls')),
    url(r'^companion/', include('companion.urls'))
)
