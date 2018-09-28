from django.db import models

from django.utils.html import mark_safe
from markdown import markdown


class Category(models.Model):
    """カテゴリ"""
    name = models.CharField(max_length=250, verbose_name='カテゴリ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日')

    def __str__(self):
        return self.name


class Blog(models.Model):
    """ブログの記事"""
    title = models.CharField(max_length=250, verbose_name='タイトル')
    content = models.TextField(verbose_name='本文')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日')
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))

    def __str__(self):
        return self.title
