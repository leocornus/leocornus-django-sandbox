from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'leocornus_django_sandbox_first.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('leocornus_django_sandbox_first.polls.urls')),
)
