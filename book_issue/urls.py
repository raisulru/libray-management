from django.urls import path, include
from .views import IssueBookView


urlpatterns = [
    path('issue-books/', IssueBookView.as_view({'get': 'list', 'post': 'create'}), name='issue-book-list'),
    path('issue-books/<pk>', IssueBookView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='issue-book-details')
]