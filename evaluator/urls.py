from django.contrib import admin
from django.urls import path
from .views import index, evaluation, pdf_export, group_evaluation

urlpatterns = [
    path('', index, name='homepage'),
    path('<str:uuid>', evaluation, name='evaluation'),
    path('export-pdf', pdf_export, name="export-pdf"),
    path('csv-file', group_evaluation, name='group-evaluation'),
]
