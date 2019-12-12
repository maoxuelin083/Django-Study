# 创建python包
# 过滤器最多两个参数
# 第一个参数永远是被过滤的那个值
# {{被过滤的值|过滤器:参数}}
# {{value | greet: 参数}}
# 将应用注册到settings.py中进行包的注册
from datetime import datetime

from django import template

register = template.Library()


@register.filter  # 进行注册
def greet(value, word):
    return value+word


@register.filter
def time_since(value):
    """

    :param value: 1分钟内  刚刚
    :return:
    """
    if not isinstance(value, datetime):
        return value
    now = datetime.now()
    timestamp = (now-value).total_seconds()
    if timestamp < 60:
        return "刚刚"

    elif timestamp >= 60 and timestamp < 60*60:
        minute = int(timestamp/60)
        return "%s分钟之前" % minute

    elif timestamp >= 60*60 and timestamp < 60*60*24:
        hour = int(timestamp/60*60)
        return "%s分钟之前" % hour

    elif timestamp >= 60*60*24 and timestamp < 60*60*24*30:
        day = int(timestamp/60*60*24)
        return "%s分钟之前" % day
    else:
        return value.strftime("%Y/%m/%d  %h:%m:%s")