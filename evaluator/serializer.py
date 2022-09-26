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


def serialize_eval(evaluation):
    return {
        "github_user": evaluation.github_user,
        "img_url": "https://avaliadorgit.com/media/" + evaluation.github_user + "_image.jpg",
        "has_readme": evaluation.has_profile_readme,
        "has_photo": evaluation.has_photo,
        "has_email": evaluation.has_email,
        "has_linkedin": evaluation.has_linkedin,
        "has_five_or_more_stacks": evaluation.has_five_or_more_stacks,
        "has_ten_or_more_stacks": evaluation.has_ten_or_more_stacks,
        "has_five_or_more_repos": evaluation.has_five_or_more_repos,
        "has_ten_or_more_repos": evaluation.has_ten_or_more_repos,
        "has_two_or_more_pinned": evaluation.has_two_or_more_pinned,
        "has_four_or_more_pinned": evaluation.has_four_or_more_pinned,
        "grade": evaluation.grade,
        "evaluation_date": evaluation.evaluation_date.strftime("%d/%m/%Y")
    }
