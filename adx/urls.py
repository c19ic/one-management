
from django.urls import path

from . import views

app_name = 'adx'

urlpatterns = [
    # ex: /adx/
    path('', views.IndexView.as_view(), name='index'),
]