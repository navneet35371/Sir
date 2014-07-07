#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from test1 import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/','app1.views.hello'),
    url(r'^hellot/','app1.views.hello_template'),
    url(r'^q=[a-z,0-9]+(?#...)','app1.views.hello_simple'),
    url(r"^$",'app1.views.home'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
