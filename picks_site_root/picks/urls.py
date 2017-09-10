from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<week_number>[0-9]+)/$', views.week_view, name="week_view")
]