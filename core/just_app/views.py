from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.views import generic
from .models import Book, Author, Publisher, Chapter
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginViews(LoginView):
    template_name = 'form.html'
    success_url = reverse_lazy('main')
    
    
class LogoutViews(LogoutView):
    template_name = 'logout.html'
    success_url = reverse_lazy('main')
    http_method_names = ['get', 'post']
    
    
class RegistrationViews(generic.CreateView):
    template_name = 'form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('main')
    model = User
    fields = '__all__'
    
    
class BookListView(generic.ListView):
    template_name = 'books.html'
    model = Book
    context_object_name = 'books'
    
class BookDetailView(generic.DetailView):
    template_name = 'detail_books.html'
    model = Book
    
    
class BookCreateView(generic.CreateView):
    template_name = 'form.html'
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')
    
    
class BookUpdateView(generic.UpdateView):
    template_name = 'form.html'
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')
    

class BookDeleteView(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('main')
    template_name = 'delete.html'
    context_object_name = 'object'


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'authors.html'
    
class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'
    
    
class PublisherListView(generic.ListView):
    template_name = 'publishers.html'
    model = Publisher
    
class PublisherDetailView(generic.DetailView):
    template_name = 'publishers_detail.html'
    model = Publisher
    
    
class ChapterListView(generic.ListView):
    template_name = 'chapters.html'
    model = Chapter
    
    
class ChapterDetailView(generic.DetailView):
    template_name = 'chapters_detail.html'
    model = Chapter
    
class ChapterCreateView(generic.CreateView):
    template_name = 'form.html'
    model = Chapter
    success_url = reverse_lazy('chapters')
    fields = '__all__'  
    
class ChapterUpdateView(generic.UpdateView):
    template_name = 'form.html'
    model = Chapter
    success_url = reverse_lazy('chapters')
    fields = "__all__"
    
    
class ChapterDeleteView(generic.DeleteView):
    template_name = 'delete_chapters.html'
    success_url = reverse_lazy('chapters')
    model = Chapter
    
