from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from webapp.views import IndexView, PdferView

import webapp.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'pdfer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', IndexView.as_view()),
    url(r'^pdfer$', PdferView.as_view()),
    # url(r'^admin/', include(admin.site.urls)),
]
