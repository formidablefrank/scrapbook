from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^login/$', views.login, name='login'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^view/(?P<book_id>[0-9]+)$', views.view, name='view'),
    url(r'^upload/(?P<book_id>[0-9]+)$', views.upload, name='upload'),
]
