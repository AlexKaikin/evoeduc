from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from apps.core.models import Post, Category, Page


class PostAdminForm(forms.ModelForm):
    preview = forms.CharField(label="Превью", widget=CKEditorUploadingWidget())
    content = forms.CharField(label="Контент", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PageAdminForm(forms.ModelForm):
    content = forms.CharField(label="Контент", widget=CKEditorUploadingWidget())

    class Meta:
        model = Page
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'published']
    list_editable = ['published']
    list_filter = ['published']
    search_fields = ['name']
    list_display_links = ['name']
    readonly_fields = ['created', 'updated']
    save_on_top = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'published']
    list_editable = ['published']
    list_filter = ['published']
    search_fields = ['name']
    list_display_links = ['name']
    readonly_fields = ['created', 'updated']
    save_on_top = True
    form = PostAdminForm


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'published']
    list_editable = ['published']
    list_filter = ['published']
    search_fields = ['name']
    list_display_links = ['name']
    readonly_fields = ['created', 'updated']
    save_on_top = True
    form = PageAdminForm
