from django.urls import path
from .views import PostList, PostDetail

app_name = 'newsportal'

urlpatterns = [
    path("news/", PostList.as_view()),
    path("news/<pk>", PostDetail.as_view(), name='news_detail'),

]