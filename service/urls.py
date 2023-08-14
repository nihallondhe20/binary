from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert_record, name='insert_record'),
    path('insert_user/', views.insert_user_record, name='insert_user_record'),
    path('list/', views.user_record_list, name='record_list'),
    path('search/', views.search_user, name='search_user'),
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
     path('edit/<int:pk>/', views.user_edit, name='user_edit'),
    
    # Add more URL patterns if needed
]
