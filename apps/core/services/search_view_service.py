from apps.core.models import Post


def get_search_list(self):
    """
    Вернет список записей по фильтру:
    - совпадение слова в заголовке
    - активные записи
    """
    post_list = Post.objects.filter(name__icontains=self.request.GET.get('q'), published='yes')
    return post_list
