from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, LikeView, AddCommentView
from . import views

urlpatterns = [
    path('', views.home, name='geodrapp-home'),
    path('about/', views.about, name='geodrapp-about'),
    path('blog/', PostListView.as_view(), name='geodrapp-blog'),
    path('like/<int:pk>/', LikeView, name='like_post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='geodrapp-add_comment'),
    path('user/<str:username>/', UserPostListView.as_view(), name='geodrapp-user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='geodrapp-post_detail'),
    path('post/new/', PostCreateView.as_view(), name='geodrapp-post_form'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='geodrapp-post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='geodrapp-post_delete'),
    path('project/', views.project, name='geodrapp-project'),
    path('service/', views.service, name='geodrapp-service'),
    path('storymap/', views.storymap, name='geodrapp-storymap'),
]



urlpatterns += staticfiles_urlpatterns()