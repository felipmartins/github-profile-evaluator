from django import forms
from .models import Evaluation, GroupCSV


class GitHubUsernameForm(forms.ModelForm):

    class Meta:
        model = Evaluation
        fields = ['github_user']

class CSVForm(forms.ModelForm):

    class Meta:
        model = GroupCSV
        fields = ['file']