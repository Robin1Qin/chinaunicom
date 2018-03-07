from django.contrib import admin

from .models import XiaoQuGuZhang

admin.site.site_header = '上海联通网络管理中心'
admin.site.site_title = '上海联通'


@admin.register(XiaoQuGuZhang)
class XiaoQuGuZhangAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'bars', 'pub_date')
    list_editable = ['account', 'bars']
    list_per_page = 10
