"""taling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views

from member.views import MyUserDetailView, TokenUserInfoAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # http://service/member/ 로 들어오는 모든 요청을 member 에 위임하여 처리한다.
    url(r'^member/', include('member.urls')),
    url(r'^regiclass/', include('regiclass.urls')),

    url(r'^token-user-info/', TokenUserInfoAPIView.as_view()),
    url(r'^user/info/(?P<pk>\d+)/', MyUserDetailView.as_view()),
    url(r'^user/info/', MyUserDetailView.as_view()),

    # url(r'^api-token-auth/', views.obtain_auth_token),
]

# API 로그인과 로그아웃 뷰에 사용되는 url 패턴
urlpatterns += [
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
urlpatterns += static('/static/', document_root='project/.static_root')
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
