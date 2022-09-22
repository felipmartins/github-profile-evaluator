from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from .views import (
    index,
    evaluation,
    group_evaluation,
    group_index,
    pdf_export,
    new_index
)
from .viewsets import GradeViewSet


urlpatterns = [
    path("", index, name="homepage"),
    path("group", group_index, name="group-homepage"),
    path("evaluation/single/<str:uuid>", evaluation, name="evaluation"),
    path("evaluation/group/<str:uuid>", group_evaluation, name="group-evaluation"),
    path(
        "evaluation/<str:type>/<str:uuid>/download",
        pdf_export,
        name="download-evaluation",
    ),
    path("grade/", GradeViewSet.as_view({"get": "list"}), name="test"),
    path("teste/", new_index, name='new-index')
]
