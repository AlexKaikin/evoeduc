from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def ajax_paginator(self, context):
    paginator = Paginator(context['object_list'], 10)
    page = self.request.GET.get('page')
    try:
        context['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        context['object_list'] = paginator.page(1)
    except EmptyPage:
        context['object_list'] = paginator.page(paginator.num_pages)
