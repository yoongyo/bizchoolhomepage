from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^subject/$', views.subject, name="subject"),
    url(r'^entrance/$', views.entrance, name="entrance"),
    url(r'^news/$', views.news, name="news"),
    url(r'^introduction/$', views.introduction, name="introduction"),
]