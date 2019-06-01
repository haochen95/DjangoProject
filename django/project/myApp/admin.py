from django.contrib import admin

# Register your models here.
from .models import Grades,Students

# 注册
# 自定义班级页面
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2

class GradesAdmin(admin.ModelAdmin):
    # 在创建班级的时候，可以同时添加两个学生
    inlines = [StudentsInfo]
    # 列表页属性
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5
    # 添加，修改页属性
    # fields = []
    fieldsets = [
        ("Number Computations", {"fields": ['ggirlnum', 'gboynum']}),
        ("Base information", {"fields": ['gname', 'gdate', 'isDelete']})
    ]


class StudentsAdmin(admin.ModelAdmin):
    # 修复布尔值显示问题
    def gender(self):
        if self.sgender:
            return "Male"
        else:
            return "Female"
    gender.short_description = "gender"

    list_display = ['pk','sname','sage',gender, 'scontend', 'sgrade', 'isDelete']
    list_per_page = 2


admin.site.register(Grades,GradesAdmin)
admin.site.register(Students,StudentsAdmin)


