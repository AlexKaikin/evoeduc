from apps.core.models import Post


def get_post_category(self):
    """ Список статей в категории по слагу"""
    slug = self.kwargs['slug']
    return Post.objects.filter(category__slug=slug, published='yes')
