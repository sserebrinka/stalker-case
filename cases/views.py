from django.shortcuts import render, get_object_or_404, redirect
from users.models import Profile
from django.contrib import messages
from .models import Cases
from users.models import Profile

# Create your views here.

def cases_view(request):
    cases = Cases.objects.all().order_by('id')
    context = balance_context(request)
    context.update({'cases': cases, 'active_page': 'cases'}) 

    return render(request, 'cases/cases.html', context)

def page1(request):
    profile = None
    if request.user.is_authenticated:
        profile = getattr(request.user, 'profile', None)
    return render(request, 'cases/page1.html', {'profile': profile, 'active_page': 'page1'})

def balance_context(request):
    profile = None
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)

    return {'profile': profile,}


def buy_case(request, case_id):
    case = get_object_or_404(Cases, id=case_id)
    profile = request.user.profile

    if profile.balance >= case.price:
        profile.balance -= case.price
        profile.add_case(case) 
        profile.save()
        messages.success(request, f"You have successfully bought {case.name}!")
    else:
        messages.error(request, "Insufficient balance!")

    return redirect('cases:cases_view')