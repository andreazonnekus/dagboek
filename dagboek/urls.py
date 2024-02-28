from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('avatar/', include('avatar.urls')),
    path('user/', include('user.urls'), name='user'),
    path('diary/', include('diary.urls'), name='diary'),
    path('admin', admin.site.urls),
]
