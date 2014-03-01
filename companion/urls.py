from django.conf.urls import patterns, url
from companion import views


urlpatterns = patterns('',
    url(r'^', views.companionView, name='companion.html')

)