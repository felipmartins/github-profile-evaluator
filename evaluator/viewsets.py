from .calculate_media import get_median
from .fetch import single_fetch_content
from .data_getter import populate_dict
from .evaluation import single_evaluation
from .create_evaluation import new_evaluation
from .models import Evaluation, MedianGrade
from .serializer import GradeSerializer, MedianSerializer
from datetime import date, timedelta
from rest_framework import viewsets
from rest_framework.response import Response

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = GradeSerializer

    def list(self, request):
        if "github_user" in request.query_params:
            user = request.query_params["github_user"]
            queryset = (
                Evaluation.objects.all()
                .filter(github_user=user)
                .order_by("-evaluation_date")
            )
            if len(queryset) > 0:
                queryset = queryset[0]
            else:
                queryset = new_evaluation(
                    single_evaluation(populate_dict(single_fetch_content(user)))
                )
            serializer = GradeSerializer(queryset)
            return Response(serializer.data)
        else:
            if len(MedianGrade.objects.all()) == 0:
                median = MedianGrade(
                    median_grade=get_median(Evaluation.objects.all().order_by("grade"))
                )
                median.save()
            else:
                median = MedianGrade.objects.all()[0]
                if median.update_date - date.today() > timedelta(days=7):
                    median.median_grade = get_median(
                        Evaluation.objects.all().order_by("grade")
                    )
                    median.save()
            serializer = MedianSerializer(median)
            return Response(serializer.data)
