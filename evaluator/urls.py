from django.contrib import admin
from django.urls import path
from .views import index, evaluation, group_evaluation, group_index

urlpatterns = [
    path('', index, name='homepage'),
    path('group', group_index, name='group-homepage'),
    path('evaluation/<str:uuid>', evaluation, name='evaluation'),
    path('evaluation/group/<str:uuid>', group_evaluation, name='group-evaluation'),
]
