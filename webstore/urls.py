from django.conf.urls import patterns, url
from webstore import views


urlpatterns = patterns('',
    url(r'^', views.webstoreView, name='webstore.html')

)
