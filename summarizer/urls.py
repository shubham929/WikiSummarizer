from django.conf.urls import patterns, url, include
from django.contrib import admin
from summarizer.views import summary, image, title, main, result

urlpatterns = patterns('',
        url(r'^$', main),
        url(r'^result', result),
        url(r'^summary/$', summary),
        url(r'^image/$', image),
        url(r'^title/$', title),
)

