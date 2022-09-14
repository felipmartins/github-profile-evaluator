from django.shortcuts import get_object_or_404
from .models import Tracker


def raise_evaluation_clicks():
    if len(Tracker.objects.all()) > 0:
        tracker = get_object_or_404(Tracker, id=1)

        tracker.clicks += 1

        tracker.save()
    else:
        ...
