from django.db.models import Q
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .models import Blog, Category
from .forms import BlogForm


class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'blogs'
    paginate_by = 10

    def get_queryset(self):
        """降順"""
        queryset = Blog.objects.order_by('-created_at')
        """キーワード検索"""
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(content__icontains=keyword))
        return queryset


class BlogDetailView(generic.DetailView):
    model = Blog
    context_object_name = 'blog'


class BlogCrateView(generic.CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """記事を投稿した時に表示するメッセージ"""
        messages.success(self.request, '保存しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '保存に失敗しました')
        return super().form_invalid(form)


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('index')


class BlogUpdateView(generic.UpdateView):
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.kwargs['pk']})


class BlogCategoryView(generic.ListView):
    model = Blog
    paginate_by = 10
    context_object_name = 'blogs'

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Blog.objects.order_by('-created_at').filter(category=category)
        return queryset


class BlogTemplateView(generic.TemplateView):
    model = Blog