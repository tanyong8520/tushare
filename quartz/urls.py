from django.conf.urls import include, url

import views
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^list', views.list,name='list'),
    url(r'^add', views.add,name='list'),
]