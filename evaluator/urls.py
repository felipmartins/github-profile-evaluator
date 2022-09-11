from django.contrib import admin
from django.urls import path
from .views import index, evaluation, pdf_export, group_evaluation, group_index, create_csv_to_evaluation

urlpatterns = [
    path('', index, name='homepage'),
    path('group', group_index, name='group-homepage'),
    path('evaluation/<str:uuid>', evaluation, name='evaluation'),
    path('export-pdf', pdf_export, name="export-pdf"),
    path('group/new', create_csv_to_evaluation, name='create-csv'),
]
