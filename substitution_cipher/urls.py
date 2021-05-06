from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^index/$', views.substitution, name='substitution'),
    url(r'^index/$', views.decryption, name='decryption')

]
