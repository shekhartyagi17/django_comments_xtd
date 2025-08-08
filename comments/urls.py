from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [

     # API endpoints for django-comments-xtd extended comments
    path('api/xtd-comments/', views.XtdCommentListCreateView.as_view(), name='xtd-comment-list-create'),
    path('api/xtd-comments/application/<str:application_id>/', views.xtd_comments_by_application, name='xtd-comments-by-application'),

    
    # API endpoints for simple comments
    # path('api/comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    # path('api/comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
    # path('api/comments/application/<str:application_id>/', views.comments_by_application, name='comments-by-application'),
    
]