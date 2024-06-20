from django.views.generic import ListView, DetailView
from .models import Post



class PostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'newsportal/news.html'
    context_object_name = 'articles'

class PostDetail(DetailView):
    model = Post
    template_name = 'newsportal/news_detail.html'
    context_object_name = 'article'
