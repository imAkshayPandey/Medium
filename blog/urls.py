from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import auth_login,auth_logout
from . import views



urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/' , views.post_detail , name='post_detail') ,
    path('post/<int:pk>/edit/' , views.post_edit , name='post_edit') ,
url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_login, name='login'),
    url(r'^logout/$',auth_logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]

