from django.conf.urls import url

from . import views

app_name = 'member'
urlpatterns = [
    url(r'^$', views.MyUserList.as_view(), name='list-or-create'),
    url(r'^(?P<pk>[0-9]+)/$', views.MyUserDetail.as_view(), name='detail'),
    url(r'^login/$', views.TalingLogin.as_view(), name='login'),
    url(r'^signup/$', views.TalingSignUp.as_view(), name='signup'),
]