"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mysite.views import BlogListView
from mysite.views import BlogDetailView
from mysite.views import BlogCrateView
from mysite.views import BlogDeleteView
from mysite.views import BlogUpdateView
from mysite.views import BlogCategoryView
from mysite.views import BlogTemplateView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', BlogListView.as_view(), name='index'),
    path('<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('create', BlogCrateView.as_view(), name='create'),
    path('<int:pk>/delete', BlogDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', BlogUpdateView.as_view(), name='update'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('category/<int:pk>', BlogCategoryView.as_view(), name='category'),
    path('about', BlogTemplateView.as_view(template_name='blog_about.html'), name='about'),
]
