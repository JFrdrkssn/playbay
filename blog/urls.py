from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('post/<int:pk>/edit_post/', views.EditPost.as_view(), name='edit_post'),
    path('post/<int:pk>/delete_post/', views.DeletePost.as_view(), name='delete_post'),
    path('like/<int:pk>', views.PostLike.as_view(), name='post_like'),
]
