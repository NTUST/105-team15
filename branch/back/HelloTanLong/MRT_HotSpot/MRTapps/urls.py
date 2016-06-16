from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='redirect'),
    url(r'^home$', views.home, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^MRT$', views.MRT, name='MRT'),
    url(r'^(?P<stopName>[\u4e00-\u9fff0-9A-Za-z._%+-]+)$', views.MRT, name='MRT'),
]
