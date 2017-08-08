from django.conf.urls import url

from . import views

app_name = 'member'
urlpatterns = [
    # Normal User
    url(r'^$', views.MyUserList.as_view(), name='list-or-create'),
    url(r'^(?P<pk>[0-9]+)/$', views.MyUserDetail.as_view(), name='detail'),

    url(r'^login/$', views.TalingLogin.as_view(), name='login'),
    url(r'^login/facebook/$', views.FaceBookLogin.as_view(), name='facebook-login'),
    url(r'^signup/$', views.TalingSignUp.as_view(), name='signup'),
    url(r'^profile/change/(?P<username>[\w-]+)/$', views.ChangeMyProfile.as_view(), name='change-profile'),

    # Tutor
    url(r'^tutor/register/$', views.TutorRegister.as_view(), name='tutor-register'),
]