from django.contrib import admin

from apps.core.models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'published']
    list_editable = ['published']
    list_filter = ['published']
    search_fields = ['name']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created', 'updated']
    save_on_top = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'published']
    list_editable = ['published']
    list_filter = ['published']
    search_fields = ['name']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created', 'updated']
    save_on_top = True
