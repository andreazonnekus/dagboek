from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('about-dev', views.about_dev, name='about_dev'),
    path('about-meitian', views.about_meitian, name='about_meitian'),
    path('admin', admin.site.urls),
    path('avatar/', include('avatar.urls')),
    path('user/', include('user.urls'), name='user'),
    path('diary/', include('diary.urls'), name='diary'),
]
