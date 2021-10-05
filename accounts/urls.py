from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('^$',views.login, name='login'),
    url('register/',views.register, name='register'),
    url('login/', views.login, name='login'),   
    url('logout/', views.logout, name='logout')
 
]