from django.conf.urls import url,patterns
from . import views
from django.conf import settings
urlpatterns=[
    url(r'^$',views.list,name='index'),
    url(r'^(?P<id>\d+)$',views.desc,name='index'),
]