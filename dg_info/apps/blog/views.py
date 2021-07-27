from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import BlogCategory, Posts


class BlogCategoryListView(ListView):
    model = Posts
    slug_field = 'slug'
    context_object_name = 'post'
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['l_menu'] = BlogCategory.objects.all()#.prefetch_related('staff_set')
        return context

class BlogCategoryDetailView(DetailView):
    model = BlogCategory
    # slug_field = 'pk'
    context_object_name = 'Category'
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Posts.objects.filter(category_id=self.object.id)
        context['l_menu'] = BlogCategory.objects.all()
        return context


class PostsDetailView(DetailView):
    model = Posts
    slug_field = 'slug'
    context_object_name = 'posts'
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['l_menu'] = BlogCategory.objects.all()
        return context


# class ContractorsListView(ListView):
#     model = Contractors
#     # slug_field = 'id'
#     context_object_name = 'Contractors'
#     template_name = 'contractors/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['l_ContractorsCategory'] = ContractorsCategory.objects.all()#.prefetch_related('staff_set')
#         return context