from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('^$',views.login, name='login'),
    url('index/',views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/', views.more, name='more'),
    

]