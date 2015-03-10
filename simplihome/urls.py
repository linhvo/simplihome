from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.api import user
from rest_framework.authtoken import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simplihome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/$', user.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', user.UserDetail.as_view()),
    # url(r'^users/register', views.UserRegister.as_view(), name='user_register'),
)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]
