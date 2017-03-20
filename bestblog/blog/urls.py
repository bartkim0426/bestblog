from django.conf.urls import url
from blog.views import index, detail


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<post_id>\d+)/$', detail, name='detail'),
]
