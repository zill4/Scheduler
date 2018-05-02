from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from scheduler import views
 
urlpatterns = [
    url(r'^schedule/$', views.ScheduleList.as_view(), name='schedule-list'),
    url(r'^schedule/(?P<pk>[0-9]+)/$', views.ScheduleDetail.as_view(), name='schedule-detail'),
]