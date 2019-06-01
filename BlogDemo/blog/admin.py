from django.contrib import admin
from .models import Blog, BlogType

# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'type_name', 'isDelete']
    list_filter = ['type_name']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['pk','title','author','createTime', 'get_read_num','lastTime', 'isDelete']
    list_filter = ['createTime']
    search_fields = ['author']

    # inlines = [BlogTypeInfo]
