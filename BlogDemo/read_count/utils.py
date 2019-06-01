import datetime
from django.contrib.contenttypes.models import ContentType
from read_count.models import ReadNum, ReadDetail
from django.utils import timezone
from django.db.models import Sum


def read_count_once_read(request, obj):
    # 总阅读数+1
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read"%(ct.model,obj.pk)
    if not request.COOKIES.get(key):
        if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
            # 存在记录
            readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)
        else:
            # 不存在记录
            readnum = ReadNum(content_type=ct, object_id=obj.pk)
        # 计数+1
        readnum.read_num +=1
        readnum.save()

    # 当天阅读数+1
        # 记录当天的访问量；逻辑类似上面的，但是我们用另外一个方法： get_or_create
        date = timezone.now().date()
        readDetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        readDetail.read_num +=1
        readDetail.save()

    return key


def get_seven_days_read_data(content_type):
    today = timezone.now().date()
    read_nums = []
    dates = []
    for i in range(6,-1,-1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        # 取出当天的阅读量
        readDatails = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = readDatails.aggregate(read_num_sum = Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums

def get_today_hot_data(content_type):
    today = timezone.now().date()
    read_details = ReadDetail.objects.filter(content_type=content_type, date=today).order_by('-read_num')
    return read_details[:7]

def get_yestoday_hot_data(content_type):
    today = timezone.now().date()
    yesterday = today - datetime.timedelta(days=1)
    read_details = ReadDetail.objects.filter(content_type=content_type, date=yesterday).order_by('-read_num')
    return read_details[:7]

def get_7_days_hot_data(content_type):
    today = timezone.now().date()
    date_limit = today - datetime.timedelta(days=7)
    read_details = ReadDetail.objects\
        .filter(content_type=content_type, date__lt=today, date__gte=date_limit)\
        .values('content_tpe', 'object_id')\
        .annotate(read_um_sum = Sum('read_num'))\
        .order_by('-read_num')
    return read_details[:7]








