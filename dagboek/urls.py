from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-me', views.about_me, name='about_me'),
    path('about-meitian', views.about_meitian, name='about_meitian'),
    path('admin', admin.site.urls),
    path('avatar/', include('avatar.urls')),
    path('user/', include('user.urls'), name='user'),
    path('diary/', include('diary.urls'), name='diary'),
]
