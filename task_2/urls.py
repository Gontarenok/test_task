from django.contrib import admin
from django.urls import path, include, re_path
from task_2.views import *

app_name = 'task_2'

urlpatterns = [
    path('/create/', ProductCreateView.as_view()),
    path('/all/', ProductListView.as_view()),
    path('/edit/<int:pk>/', ProductDetailView.as_view()),
    # path('/json/', ExampleView.as_view()),
    path('/upload/', FileUploadView.as_view()),
    # re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view())
]
