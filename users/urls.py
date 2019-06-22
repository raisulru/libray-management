from django.urls import path, include
from .views import UsersView


urlpatterns = [
    path('users/', UsersView.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<pk>', UsersView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-details')
]