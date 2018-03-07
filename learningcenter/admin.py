from django.contrib import admin

from .models import Catagory, Article, Comment

admin.site.site_header = '上海联通网络管理中心'
admin.site.site_title = '上海联通'


@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ['name']
    list_per_page = 10


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',  'created')
    list_display_links = ['title']
    list_per_page = 10


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog','name', 'content', 'created')
    list_display_links = ['blog']
    list_editable = ['name', 'content']
    list_per_page = 10
