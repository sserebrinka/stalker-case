from django.urls import path
from . import views


app_name = 'cases'

urlpatterns = [
    path('', views.cases, name='cases'),
    path('page1', views.page1, name='page1')
]
  