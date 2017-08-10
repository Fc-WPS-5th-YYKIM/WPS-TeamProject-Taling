from django.conf.urls import url

from . import views

app_name = 'member'
urlpatterns = [
    # MyUser
    url(r'^$', views.MyUserList.as_view(), name='list-or-create'),
    url(r'^(?P<pk>[0-9]+)/$', views.MyUserDetail.as_view(), name='detail'),

    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^login/facebook/$', views.FaceBookLoginView.as_view(), name='facebook-login'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^profile/(?P<user_pk>[0-9]+)/$', views.QueryMyProfile.as_view(), name='query-my-profile'),
    url(r'^profile/change/(?P<pk>[0-9]+)/$', views.EditOrDeleteMyProfile.as_view(), name='edit-or-delete-my-profile'),

    # Tutor
    url(r'^tutor/register/$', views.TutorRegister.as_view(), name='tutor-register'),
]