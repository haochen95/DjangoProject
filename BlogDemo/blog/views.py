import datetime
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog, BlogType
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count,Sum
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from read_count.models import ReadNum
from read_count.utils import read_count_once_read,get_seven_days_read_data,\
                                get_today_hot_data,get_yestoday_hot_data,get_7_days_hot_data


def get_blog_list_common_data(request, blog_all_list):
    paginator = Paginator(blog_all_list, settings.EACH_PAGE_BLOGS_NUMBER)
    page_num = request.GET.get('page', 1)  # 获取url参数
    page_of_blogs = paginator.get_page(page_num) # 获取当前博客对象
    current_page_num = page_of_blogs.number # 获取当前页码
    # 获取当前页码前后各2页的页面范围
    page_range = list(range(max(current_page_num-2,1), current_page_num)) + \
                 list(range(min(current_page_num+2,paginator.num_pages)+1, current_page_num))

    context = {}
    context['blog'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.annotate(blog_count = Count('blog'))  # 获取博客分类的对象博客数量:annotate(注释)
    context['blog_dates'] = Blog.objects.dates('createTime', 'month', order = "DESC")
    return context

def index(request):
    return HttpResponse("good")

def get_7_days_hot_blogs():
    today = timezone.now().date()
    date_limit = today - datetime.timedelta(days=7)
    blogs = Blog.objects\
        .filter(read_details__date__lt=today, read_details__date__gte=date_limit)\
        .values('id','title')\
        .annotate(read_num_sum = Sum('read_details__read_num'))\
        .order_by('-read_num_sum')
    return blogs[:7]

def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, res = get_seven_days_read_data(blog_content_type)

    # 获取7天热门博客的缓存数据
    h7 = cache.get('seven_day_hot_data')
    if h7 is None:
        h7 = get_7_days_hot_blogs()
        cache.set('seven_day_hot_data', h7,3600)

    context = {}
    context['read_nums'] = res
    context['dates'] = dates
    context['today_hot_data'] = get_today_hot_data(blog_content_type)
    context['yesterday_hot_data'] = get_yestoday_hot_data(blog_content_type)
    context['seven_day_hot_data'] = get_7_days_hot_blogs()
    return render(request, 'home.html', context)


def blog_list(request):
    blogList = Blog.objects.filter(isDelete=False)
    context = get_blog_list_common_data(request, blogList)
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, blog_pk):
    context = {}
    blogs = get_object_or_404(Blog, pk = blog_pk)
    read_cookie_key = read_count_once_read(request,blogs)

    # 取当前打开博客的时候，获取大于当前博客创建时间的博客,并取最后一条==上一条博客
    context['previous_blog'] = Blog.objects.filter(createTime__gt=blogs.createTime).last()
    context['next_blog'] = Blog.objects.filter(createTime__lt=blogs.createTime).first()
    context['blog'] = blogs
    response = render(request, 'blog/blog_detail.html', context)
    response.set_cookie(read_cookie_key, 'true') # 阅读cookie标记
    return response

def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk = blog_type_pk)
    blog_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_list_common_data(request, blog_all_list)
    context['blog_type'] = blog_type
    return render(request, 'blog/blogs_with_type.html', context)

def blogs_with_date(request, year, month):
    blog_all_list = Blog.objects.filter(createTime__year=year, createTime__month=month)
    context = get_blog_list_common_data(request, blog_all_list)
    context['blogs_with_date'] = '%s年%s月'%(year, month)
    return render(request, 'blog/blog_with_date.html', context)
