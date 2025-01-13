from django.shortcuts import render
from .models import Blog, Article, Tag, News, Poll
from django.views.generic import ListView

class BlogsView(ListView):
    template_name = 'blogs.html'
    model = Blog
    context_object_name = 'blogs'


class ArticlesView(ListView):
    template_name = 'articles.html'
    model = Article
    context_object_name = 'articles'


class TagsView(ListView):
    template_name = 'tags.html'
    model = Tag
    context_object_name = 'tags'


class NewsView(ListView):
    template_name = 'news.html'
    model = News
    context_object_name = 'news'


class PollsView(ListView):
    template_name = 'polls.html'
    model = Poll
    context_object_name = 'polls'