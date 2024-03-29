from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.EntryListView.as_view(), name='entry_list'),
    path('<int:pk>', views.EntryDetailView.as_view(), name='entry_detail'),
    path('create/', views.EntryCreateView.as_view(), name='entry_create'),
    path('<int:pk>/delete/', views.EntryDeleteView.as_view(), name='entry_delete'),
    path('<int:pk>/update/', views.EntryUpdateView.as_view(), name='entry_update')
]
