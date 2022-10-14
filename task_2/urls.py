from django.contrib import admin
from django.urls import path, include
from task_2.views import *

app_name = 'task_2'

urlpatterns = [
    path('/create/', ProductCreateView.as_view()),
    path('/all/', ProductListView.as_view()),
    path('/edit/<int:pk>/', ProductDetailView.as_view()),
]
