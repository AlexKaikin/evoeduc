from apps.core.models import Post


def get_post_all():
    """ Список всех статей """
    return Post.objects.filter(published='yes')
