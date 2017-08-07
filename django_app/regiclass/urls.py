from django.conf.urls import url

from . import views

app_name = 'regiclass'
urlpatterns = [
    url(r'^class/make/$', views.LectureMake.as_view(), name='make_class'),
    url(r'^class/list/$', views.LectureList.as_view(), name='list_class'),
]
