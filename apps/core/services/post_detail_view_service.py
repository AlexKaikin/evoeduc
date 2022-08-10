from apps.core.models import Post


def get_post_detail(self):
    """ Детализация статьи """
    slug = self.kwargs['slug']
    return Post.objects.filter(slug=slug, published='yes')
