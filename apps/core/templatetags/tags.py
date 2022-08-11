from django import template

from apps.core.models import Category, Page

register = template.Library()


@register.simple_tag()
def get_category_tag():
    """
    Вернет список категорий по фильтру:
    - активные
    """
    return Category.objects.filter(published='yes')


@register.simple_tag()
def get_page_tag():
    """
    Вернет список страниц по фильтру:
    - активные
    """
    return Page.objects.filter(published='yes')
