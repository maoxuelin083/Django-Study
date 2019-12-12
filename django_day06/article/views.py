from django.http import HttpResponse

# Create your views here.
from article.models import Article, Tag


def index(request):
    article = Article(title='三国演义', content='三国演义是罗贯中的得意之作')
    # tag = Tag(name='四大名著')
    # article.tag_set.all(tag)
    article.save()
    return HttpResponse("index")


def index1(request):
    # article = Article.objects.get(pk=1)
    tag = Tag(name='四大名著')
    # article.tag_set.add(tag)
    tag.save()
    return HttpResponse("index1")


def index2(request):
    article = Article.objects.get(pk=1)
    tag = Tag.objects.get(pk=1)
    article.tag_set.add(tag)
    tag.save()
    return HttpResponse('index2')


def index3(request):
    article = Article.objects.first()
    tags = article.tag_set.all()  # 多对多的关系写在 tag下面
    # print(tags)   # <QuerySet [<Tag: Tag object (1)>]>
    for tag in tags:
        print("%s:%s" % (tag.id, tag.name))
    return HttpResponse("index3")


def index4(request):
    article = Article.objects.first()
    tags = article.tag_set.all()
    for tag in tags:
        print(tag)
    return HttpResponse("index4")