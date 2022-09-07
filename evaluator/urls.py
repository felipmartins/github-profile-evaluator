from django.contrib import admin
from django.urls import path
from .views import index, evaluation, pdf_export

urlpatterns = [
    path('', index, name='homepage'),
    path('<int:id>', evaluation, name='evaluation'),
    path('export-pdf', pdf_export, name="export-pdf")
]
