from django import template

register = template.Larbry()
@register.filter
def test_filter(value):   # 过滤器至多有两个参数   第一个参数永远是被过滤的内容
    word = value
    if word == "cnm":
        return "文明用语"
    else:
        return word





