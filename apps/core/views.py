from django.views.generic import ListView, DetailView

from apps.core.models import Post
from apps.core.services.category_view_service import get_post_category
from apps.core.services.index_view_service import get_post_all
from apps.core.services.post_detail_view_service import get_post_detail


class IndexView(ListView):
    """ Главная страница, вывод всех статей """
    model = Post
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_index'] = True
        return context

    def get_queryset(self):
        return get_post_all()


class CategoryView(ListView):
    """ Страница статей по выбранной категории """
    model = Post
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_category'] = True
        return context

    def get_queryset(self):
        return get_post_category(self)


class PostDetailView(DetailView):
    """ Детализация статьи """
    model = Post
    template_name = 'core/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_category'] = True
        return context

    def get_queryset(self):
        return get_post_detail(self)
