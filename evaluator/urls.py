from django.contrib import admin
from django.urls import path
from .views import index, evaluation

urlpatterns = [
    path('', index, name='homepage'),
    path('<int:id>', evaluation, name='evaluation'),
]
