from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('index/',views.index, name='index'),
    url(r'^more/(?P<pk>[0-9]+)/', views.more, name='more'),
    url(r'^faultform/(?P<pk>[0-9]+)/', views.faultform, name='faultform'),
    url(r'^create/(?P<pk>[0-9]+)/',views.create, name='create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)