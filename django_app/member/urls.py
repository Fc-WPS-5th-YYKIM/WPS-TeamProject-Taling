from django.conf.urls import url

from . import views

app_name = 'member'
urlpatterns = [
    # MyUser
    url(r'^$', views.MyUserList.as_view(), name='list-or-create'),
    # url(r'^(?P<pk>[0-9]+)/$', views.MyUserDetailView.as_view(), name='detail'),

    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^login/facebook/$', views.FaceBookLoginView.as_view(), name='facebook-login'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^profile/(?P<user_pk>[0-9]+)/$', views.MyProfileView.as_view(), name='my-profile'),
    url(r'^change/password/(?P<user_pk>[0-9]+)/$', views.ChangePasswordView.as_view(), name='change-password'),

    # Tutor
    url(r'^tutor/register/$', views.TutorRegister.as_view(), name='tutor-register'),
]