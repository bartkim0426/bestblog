from django.conf.urls import url
from blog.views import stack, stackdetail, archives, auth_menu


urlpatterns = [ 
    url(r'^technology-stack/$', stack, name='stack'),
    url(r'^technology-stack/(?P<stack_slug>\w+)/$', stackdetail, name='stack-detail'),
    url(r'^archives/$', archives, name='archives'),
    url(r'^auth_menu/', auth_menu, name='auth'),
    ]
