from django.urls import include, re_path, path
from django.contrib import admin
# from django.conf.urls import url
# from django.urls import include, path

from Train_Website.views import register, login_view, logout_view

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^register/$', register, name='register'),
    re_path(r'^login/$', login_view, name = 'login'),
    re_path(r'^logout/$', logout_view),
    path('', include('resume_page.urls')),
    path('admin/', admin.site.urls),
    path('', include('Train_Website.urls')),
]
