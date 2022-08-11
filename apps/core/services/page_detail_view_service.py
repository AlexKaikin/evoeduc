from apps.core.models import Page


def get_page_detail(self):
    """ Детализация страницы """
    slug = self.kwargs['slug']
    return Page.objects.filter(slug=slug, published='yes')
