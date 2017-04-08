from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from .views import home


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('blog.urls.posts', namespace='posts')),
     url(r'^menu/', include('blog.urls.menu', namespace='menu')),
     url(r'^auth/', include('blog.urls.auth', namespace='auth')),
    url(r'^$', home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar  
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
