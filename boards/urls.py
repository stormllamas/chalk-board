from django.urls import path
from . import views


app_name = 'boards'
urlpatterns = [
    path('', views.BoardListView.as_view(), name='home'),
    path('<int:pk>/topics/', views.TopicListView.as_view(), name='board_topics'),
    path('new_topic/<int:pk>/', views.new_topic, name='new_topic'),
    path('<int:pk>/topic/<int:topic_pk>/', views.PostListView.as_view(), name='topic_posts'),
    path('<int:pk>/topic/<int:topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    path('<int:pk>/topic/<int:topic_pk>/post/<int:post_pk>/edit/', views.PostUpdateView.as_view(), name='edit_post')
]