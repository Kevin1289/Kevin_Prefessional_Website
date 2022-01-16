# from django.conf.urls import url
from django.urls import include, re_path, path
# from django.urls import include, path
from . import views
from .views import test

urlpatterns = [
    re_path(r'^test/$', views.test),
    path('Train_Choose_Service', views.Train_Choose_Service, name='Train_Choose_Service'),
    re_path(r'^all_stops/$', views.all_stops, name='all_stops'),
    re_path(r'^common_stations/$', views.common_stations, name='common_stations'),
    path('history', views.History, name='history'),
    path('logout', views.logout_view, name='logout'),
]
