from django.urls import path
from .views import BlogCategoryListView, BlogCategoryDetailView, PostsDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogCategoryListView.as_view(), name='main'),
    path('<slug:slug>/', BlogCategoryDetailView.as_view(), name='group-blog'),
    path('<slug:cut>/<slug:slug>/', PostsDetailView.as_view(), name='postView'),

]