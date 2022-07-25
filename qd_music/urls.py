from django.urls import path 
from . import views
from django.contrib import admin
admin.autodiscover()
from . import views




urlpatterns = [
    path('', views.index, name='homepage'),
    

     ## THIS HAS TO BE LAST##
    #-Blog Functionality-#
    path('admin/', admin.site.urls),
    path('gigs/', views.PostList.as_view(), name='gigs'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
    ##THIS HAS TO BE LAST##
]