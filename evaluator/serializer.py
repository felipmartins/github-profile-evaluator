from .models import Evaluation, MedianGrade
from rest_framework import serializers


class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evaluation
        fields = ["grade"]


class MedianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedianGrade
        fields = ["median_grade"]
