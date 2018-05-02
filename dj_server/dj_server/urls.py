from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from dj_server import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='FHDA Scheduler API', description='RESTful API for FHDA Scheduler')),
 
    url(r'^$', views.api_root),
    #url(r'^reviews/', include(('reviews.urls', 'reviews'), namespace='reviews')),
    url(r'^', include(('users.urls','users'), namespace='users')),
    url(r'^', include(('scheduler.urls','scheduler'), namespace='scheduler')),
]