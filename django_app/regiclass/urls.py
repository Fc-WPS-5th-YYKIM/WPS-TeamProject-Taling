from django.conf.urls import url

from . import views

app_name = 'regiclass'
urlpatterns = [
    url(r'^class/make/$', views.LectureMake.as_view(), name='make_class'),
    url(r'^class/list/$', views.LectureList.as_view(), name='list_class'),
    url(r'^class/detail/$', views.LectureDetail.as_view(), name='detail_class'),
    url(r'^review/make/$', views.ReviewMake.as_view(), name='make_review'),
    url(r'^review/list/$', views.ReviewList.as_view(), name='list_review'),
]
