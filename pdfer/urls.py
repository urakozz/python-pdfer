from django.conf.urls import include, url
from django.contrib import admin

import webapp.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'pdfer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', webapp.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
