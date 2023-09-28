from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.core.paginator import Paginator
from .models import *
from .filters import PostFilter
from .forms import NewsForm

class PostsList(ListView):
    model = Post # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html' # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts' # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id') # выводим в обратном порядке
    paginate_by = 10 # поставим постраничный вывод в 10 элементов
    
class PostList(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostsSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'filter'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

class PostsAdd(CreateView):
    template_name = 'add.html'
    form_class = NewsForm
    success_url = '/news/'


class PostEdit(UpdateView):
    template_name = 'edit.html'
    form_class = NewsForm
    success_url = '/news/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


def home(request):
    return render(request, 'home.html')
