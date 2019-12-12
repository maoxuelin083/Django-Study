from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# def add_users(request):
#     Users.objects.create(name="小敏", age=14, sex=1)
#     return HttpResponse("success")
#
#
# def add_tag(request):
#     user = Users.objects.first()
#     article = Article(title="西游记", content="罗贯中紧耦合")
#     article.save()
#     user.article_set.add(article)
#     return HttpResponse("success")