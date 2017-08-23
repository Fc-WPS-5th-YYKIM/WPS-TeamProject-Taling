from django.conf.urls import url

from . import views

app_name = 'regiclass'
urlpatterns = [
    url(r'^class/make/$', views.LectureMake.as_view(), name='make_class'),
    url(r'^class/update/$', views.LcetureUpdate.as_view(), name='update_class'),
    url(r'^class/list/$', views.LectureList.as_view(), name='list_class'),
    url(r'^class/detail/$', views.LectureDetail.as_view(), name='detail_class'),
    url(r'^class/likeclass/$', views.LikeLecture.as_view(), name='like_class'),
    url(r'^review/make/$', views.Reviews.as_view(), name='make_review'),
    url(r'^review/list/$', views.Reviews.as_view(), name='list_review'),

    # 수강신청
    url(r'^lecture/register/(?P<lecture_pk>[0-9]+)/$', views.EnrollmentView.as_view(), name='enrollment'),
    # url(r'^talent/guide/(?P<slug>[-\w\d]+)/$', views.TalenteGuideView.as_view(), name='talent-guide'),
    # url(r'^talent/check/(?P<slug>[-\w\d]+)/$', views.CheckLocationView.as_view(), name='talent-check'),
    # url(r'^talent/apply/(?P<slug>[-\w\d]+)/$', views.ApplyMyTalentView.as_view(), name='talent-apply'),
    # url(r'^talent/auth/(?P<slug>[-\w\d]+)/$', views.StudentAuthView.as_view(), name='talent-auth'),
    # url(r'^talent/pay/(?P<slug>[-\w\d]+)/$', views.ClassPaymentView.as_view(), name='talent-pay'),
]
