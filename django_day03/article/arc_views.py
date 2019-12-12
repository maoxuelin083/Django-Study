from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "username": "mxl",
    }
    return render(request, 'include.html', context=context)


def school(request):
    context = {
        "school": "千峰"
    }
    return render(request, 'school.html', context=context)


def company(request):
    context = {
        "company": "毛毛集团"
    }
    return render(request, 'company.html', context=context)


def book(request):
    return render(request, 'book.html')
