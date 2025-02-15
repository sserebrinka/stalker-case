from django.urls import path
from . import views
from .views import buy_case, cases_view


app_name = 'cases'

urlpatterns = [
    path('', views.cases_view, name='cases_view'),
    path('page1', views.page1, name='page1'),
    path('buy/<int:case_id>/', buy_case, name='buy_case'),
]
  