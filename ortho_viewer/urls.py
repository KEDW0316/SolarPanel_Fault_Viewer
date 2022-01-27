from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^index/',views.index, name='index'),
    url('gohome/',views.gohome, name='gohome'),
    url(r'^more/(?P<pk>[0-9]+)/', views.more, name='more'),
    url(r'^faultform/(?P<pk>[0-9]+)/', views.faultform, name='faultform'),
    url(r'^create/(?P<pk>[0-9]+)/',views.create, name='create'),
    url(r'^createfaultmark/(?P<pk>[0-9]+)/(?P<pk2>[0-9]+)',views.create_faultmark, name='create_faultmark'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)