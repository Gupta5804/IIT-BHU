
#!python
# authtest/urls.py
from django.conf.urls import include, url
from django.contrib import admin
# Add this import

from django.contrib.auth import views
from log import views as core_views
from log.forms import LoginForm
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('log.urls')),

    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
    url(r'^signup/',core_views.signup,name='signup'),
    url(r'^edit_profile/(?P<pk>\d+)/$', core_views.edit_user, name='account_update'),

]
urlpatterns += staticfiles_urlpatterns()
