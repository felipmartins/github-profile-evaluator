from django.shortcuts import get_object_or_404
from .models import Tracker


def raise_evaluation_clicks():
    if len(Tracker.objects.all()) > 0:
        tracker = get_object_or_404(Tracker, id=1)

        tracker.clicks += 1

        tracker.save()
    else:
        ...


def raise_group_evaluation_clicks():
    if len(Tracker.objects.all()) > 0:
        tracker = get_object_or_404(Tracker, id=2)

        tracker.clicks += 1

        tracker.save()
    else:
        ...


def raise_single_download_clicks():
    if len(Tracker.objects.all()) > 0:
        tracker = get_object_or_404(Tracker, id=3)

        tracker.clicks += 1

        tracker.save()
    else:
        ...


def raise_group_download_clicks():
    if len(Tracker.objects.all()) > 0:
        tracker = get_object_or_404(Tracker, id=4)

        tracker.clicks += 1

        tracker.save()
    else:
        ...
