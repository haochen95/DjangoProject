from django.db import models

# Create your models here.

class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = "grades"
        ordering = ['id']

class StudentsManager(models.Manager):
    # 只显示isDelete为假的数据
    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(isDelete = False)

class Students(models.Model):

    # 自定义管理器
    stuObj = models.Manager()  # 默认自定义管理器
    stuObj2 = StudentsManager()  # 过滤器管理器

    # 1(班级)对多(学生)，外键写在多的里面
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    sgrade = models.ForeignKey('Grades', on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)

    # 添加新的方法
    def __str__(self):
        return self.sname

    class Meta:
        db_table = "students"
        ordering = ['id']

    # 定义一个类方法创建对象,cls表示Students
    @classmethod
    def createStudent(cls, name,age,gender,contend,grade,isD=False):
        stu = cls(sname = name,sage=age,sgender=gender,scontend = contend, isDelete=isD, sgrade = grade)
        return stu


