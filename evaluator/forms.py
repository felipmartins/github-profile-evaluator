from django import forms
from .models import Evaluation


class GitHubUsernameForm(forms.ModelForm):

    class Meta:
        model = Evaluation
        fields = ['github_user']