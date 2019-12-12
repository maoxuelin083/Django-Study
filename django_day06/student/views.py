
from django.db.models import Avg, Count, Sum, Q, F, Max, Min
from django.http import HttpResponse

# Create your views here.
from student.models import Score, Student, Teacher, Course


def index1(request):
    rows = Student.objects.annotate(avg=Avg("score__number")).values('id', 'name', 'avg')
    for row in rows:
        print(row)
    return HttpResponse("index1")


def index2(request):
    rows = Student.objects.annotate(total_course=Count("score__course_id"), nums=Sum("score__number")).values('id', 'name', 'total_course', 'nums')
    for row in rows:
        print(row)
    return HttpResponse("index2")


def index3(request):
    rows = Teacher.objects.filter(name__startswith="李").count()
    print(rows)
    return HttpResponse("index3")


def index4(request):
    rows = Student.objects.exclude(score__course_id__teacher_id__name="李老师").values('id', 'name')
    for row in rows:
        print(row)
    return HttpResponse("index4")


def index5(request):
    rows = Student.objects.filter(score__course_id__in=[1, 2]).distinct().values('id', 'name')
    for row in rows:
        print(row)
    return HttpResponse("index5")






























# def index1(request):
#     rows = Student.objects.annotate(avg_num=Avg('score__number')).filter(avg_num__gt=60).values('id','avg_num')
#     for row in rows:
#         print(row)
#     return HttpResponse("index1")
#
#
# def index2(request):
#     rows = Student.objects.annotate(course_name=Count('score__course_id'), total_score=Sum('score__number')).values("id", "name", "course_name", "total_score")
#     for row in rows:
#         print(row)
#     return HttpResponse("index2")
#
#
# def index3(request):
#     rows = Teacher.objects.filter(name__startswith="李").count()
#     print(rows)
#     return HttpResponse("index3")
#
#
# def index4(request):
#     rows = Student.objects.exclude(score__course_id__teacher__name="李老师").values('id', 'name')
#     print(rows)
#     return HttpResponse("index4")
#
#
# def index5(request):
#     rows = Student.objects.filter(score__course_id__in=[1, 2]).distinct().values('id', 'name')
#     print(rows)
#     return HttpResponse("index5")
#
#
# def index6(request):
#     rows = Student.objects.annotate(num=Count("score__course_id", filter=Q(score__course_id_teacher_id_name="黄老师")))
#     print(rows)
#     return HttpResponse("index6")
#
#
# # √
# def index7(request):
#     rows = Student.objects.exclude(score__number__gt=60).values('id', 'name')
#     for row in rows:
#         print(row)
#     return HttpResponse('index7')
#
#
# def index8(request):
#     # score__course_id找到每门课的id  就是每个学生对应的course_id数量
#     rows = Student.objects.annotate(num=Count("score__course_id")).filter(num__lt=Course.objects.count()).values('id')
#     for row in rows:
#         print(row)
#     return HttpResponse('index8')
#
#
# # √
# def index9(request):
#     rows = Student.objects.annotate(avg=Avg("score__number")).values('id', 'name', 'avg').order_by('-avg')
#     for row in rows:
#         print(row)
#     return HttpResponse('index9')
#
#
# def index10(request):
#     # 找到每一个course的信息
#     rows = Course.objects.annotate(max=Max("score__number"), min=Min("score__number")).values('id','name','max','min')
#     for row in rows:
#         print(row)
#     return HttpResponse('index10')
#
#
# # √
# def index11(request):
#     rows = Course.objects.annotate(avg=Avg("score__number")).values('id','avg').order_by('-avg')
#     for row in rows:
#         print(row)
#     return HttpResponse('index11')
#
#
# def index12(request):
#     rows = Student.objects.aggregate(man_gender=Count("gender", filter=Q(gender=1)), wman_gender=Count("gender", filter=Q(gender=2)))
#     # for row in rows:
#     print(rows)
#     return HttpResponse('index12')
#
#
# def index13(request):
#     rows = Score.objects.filter(course_id__teacher_id__name="黄老师").update(number=F("number")+5)
#     for row in rows:
#         print(row)
#     return HttpResponse('index13')
#
#
# def index14(request):
#     rows = Student.objects.annotate(score_num=Count("score__number", filter=Q(score__number__lt=60))).filter(score_num__gt=2).values('id', 'name')
#     print(rows.query)
#     for row in rows:
#         print(row)
#     return HttpResponse('index14')
#
#
# def index15(request):
#     rows = Course.objects.annotate(student_num=Count("score__student_id")).values('id', 'name', 'student_num')
#     for row in rows:
#         print(row)
#     return HttpResponse('index15')