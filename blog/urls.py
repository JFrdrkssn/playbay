from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:id>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<int:id>', views.PostLike.as_view(), name='post_like'),
]
