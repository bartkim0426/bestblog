from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from blog.views import index, detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/$', index, name='index'),
    url(r'^post/(?P<post_id>\d+)/$', detail, name='detail'),
]

if settings.DEBUG:
    import debug_toolbar  
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
