from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

# Create your models here.

class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)

    # 指向contenttype模型
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    # 指定id
    object_id = models.PositiveIntegerField()
    # 将上面的统一起来形成通用的外键
    content_object = GenericForeignKey('content_type', 'object_id')

class Read_Count_father():
    # 获取阅读数
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)  # 拿到blog这条的contenttype记录
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk) # 通过contenttype和id查readnum
            return readnum.read_num
        except Exception as e:
            return 0

class ReadDetail(models.Model):
    date = models.DateField(default=timezone.now)
    read_num = models.IntegerField(default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')