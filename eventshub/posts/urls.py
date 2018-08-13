from django.conf.urls import url
from django.contrib import admin

from .views import (
    home, 
    event_add,
    event_update,
    event_delete,
    event_details,   
)

urlpatterns = [
    url(r'^$', home, name="list"),
    url(r'^add/$', event_add),
    url(r'^(?P<id>\d+)/edit/$', event_update, name="update"),
    url(r'^^(?P<id>\d+)/delete/$', event_delete),
    url(r'^(?P<id>\d+)/$', event_details, name="detail"),
]