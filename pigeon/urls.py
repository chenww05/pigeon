from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mankey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^planner/', include('planner.urls', namespace="planner")),
    url(r'^admin/', include(admin.site.urls)),
)
