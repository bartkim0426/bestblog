from django.conf.urls import url
from blog.views import signup, login, logout, mypage


urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^my/page/$', mypage, name="mypage"),
        ]
