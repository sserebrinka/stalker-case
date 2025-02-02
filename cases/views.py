from django.shortcuts import render

# Create your views here.

def cases(request):
    return render(request, 'cases/cases.html', {'active_page': 'cases'})