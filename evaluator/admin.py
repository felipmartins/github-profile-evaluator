from django.contrib import admin
from .models import GroupCSV, GroupEvaluation, Tracker, Evaluation

admin.site.register(Tracker)
admin.site.register(Evaluation)
admin.site.register(GroupCSV)
admin.site.register(GroupEvaluation)
