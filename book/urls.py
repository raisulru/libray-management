from django.urls import path, include
from .views import BookView


urlpatterns = [
    path('books/', BookView.as_view({'get': 'list', 'post': 'create'}), name='book-list'),
    path('books/<pk>', BookView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='book-details')
]