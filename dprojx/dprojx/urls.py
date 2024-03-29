# dprojx/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from dappx import views
from chat.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^dappx/',include('dappx.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^$', index, name='homepage'),  
]    
