from django.urls import path
from .views import ListAuthorAPIView, ListPostAPIView, CreateAuthorAPIView, UpdateAuthorAPIView, DeleteAuthorAPIView, members, register,user_login, my_details, user_logout

urlpatterns = [
    path("author-list/", ListAuthorAPIView.as_view(), name="author_list"),
    path("post-list/", ListPostAPIView.as_view(), name= "post_list" ),
    path("create-author/",CreateAuthorAPIView.as_view(), name= "create_author" ),
    path("update-author/<int:pk>", UpdateAuthorAPIView.as_view(), name= "update_author" ),
    path("delete/<int:pk>", DeleteAuthorAPIView.as_view(), name="delete_author"),
    path("test/",members, name= "members"),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('details/', my_details, name="my_details"),\
    path('logout/', user_logout, name='logout'),
]