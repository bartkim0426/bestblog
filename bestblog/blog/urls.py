from django.conf.urls import url

from blog.views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<post_id>\d+)/$', detail, name='detail'),
    url(r'^new/$', new, name='new'),
    url(r'^create/$', create, name='create'),
    url(r'^(?P<post_id>\d+)/edit/$', edit, name='edit'),
    url(r'^(?P<post_id>\d+)/update/$', update, name='update'),
    url(r'^(?P<post_id>\d+)/delete/$', delete, name='delete'),
    # menus 
    url(r'^technology-stack/$', stack, name='stack'),
    url(r'^etc/$', etc, name='etc'),
    url(r'^archives/$', archives, name='archives'),
    # comments
    url(r'^(?P<post_id>\d+)/comments/new/$', new_comments, name='new-comments'),
    url(r'^(?P<post_id>\d+)/comments/(?P<comment_id>\d+)/edit/$', edit_comments, name='edit-comments'),
    url(r'^(?P<post_id>\d+)/comments/(?P<comment_id>\d+)/update/$', update_comments, name='update-comments'),
    url(r'^(?P<post_id>\d+)/comments/(?P<comment_id>\d+)/delete/$', delete_comments, name='delete-comments'),
] 
