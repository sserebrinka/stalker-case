from django.shortcuts import render

# Create your views here.

def cases(request):
    return render(request, 'cases/cases.html', {'active_page': 'cases'})

def page1(request):
    return render(request, 'cases/page1.html', {'active_page': 'page1'})