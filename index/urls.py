from django.urls import path
from django.views.generic import ListView, DetailView
from . import views
from index.models import *

urlpatterns = [
    path('', views.index, name='index'),
    path('chart/', views.chart, name='chart'),
    path('ipo/', views.ipo, name='ipo'),
    path('stock/', views.stock, name='stock'),
    path('bank/', views.bank, name='bank'),
    path('book_list/', ListView.as_view(queryset=Book.objects.all().order_by("author")), name='book_list.html'),
    path('message_list/', views.message_list, name='message_list.html'),
]

# ListView.as_view(queryset=Message.objects.all().order_by("-date"))
