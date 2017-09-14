from django.conf.urls import url,include
from django.contrib import admin
from. import views
urlpatterns=[
    url(r'^$',view=views.lb,name="logbook"),
    url(r'^login$',view=views.login,name="login"),
    url(r'^add$',view=views.add,name='add'),
    url(r'^view$',view=views.view,name='view'),
    url(r'^view/(?P<username>[A-Za-z0-9]+)$',view=views.viewbyusername,name='view'),
    url(r'^requestid$',view=views.requestid,name='requestid')

]