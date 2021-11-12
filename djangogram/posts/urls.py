from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    # /posts/
    path('', views.index, name='index'),

    # /posts/create/
    path('create/', views.post_create, name='post_create'),

    # /posts/3/update/
    path('<int:post_id>/update/', views.post_update, name="post_update"),

    # /posts/1/comment_create/
    path('<int:post_id>/comment_create', views.comment_create, name="comment_create"),

    # /posts/1/comment_delete/
    path('<int:comment_id>/comment_delete', views.comment_delete, name="comment_delete"),
]
