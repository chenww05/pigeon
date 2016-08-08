from django.conf.urls import url

from . import views

app_name = 'planner'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<wedding_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /planner/5/results/
    url(r'^(?P<wedding_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /planner/5/vote/
    url(r'^(?P<wedding_id>[0-9]+)/vote/$', views.vote, name='vote'),
]