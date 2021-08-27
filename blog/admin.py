from django.contrib import admin

from .models import Post


# Register your models here.
# admin.site.register(Post)

# 定制模型显示

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 显示指定字段
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # 检索字段
    search_fields = ('title', 'body')
    # 过滤字段
    list_filter = ('status', 'publish', 'author')
    # 填充字段(不支持中文)
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author', )
    # 默认现在最近日期的数据
    date_hierarchy = 'publish'
    # 排序规则
    ordering = ('status', 'publish')
