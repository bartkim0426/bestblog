from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from .views import home


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('blog.urls', namespace='posts')),
    url(r'^$', home),
]

if settings.DEBUG:
    import debug_toolbar  
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
