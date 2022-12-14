import uuid
from django.db import models


class Tracker(models.Model):
    name = models.CharField(max_length=25)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - clicks: {self.clicks}"


class Evaluation(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    github_user = models.CharField(max_length=50)
    evaluation_date = models.DateField(auto_now_add=True)
    has_profile_readme = models.BooleanField(default=True)
    has_photo = models.BooleanField()
    has_email = models.BooleanField()
    has_linkedin = models.BooleanField()
    stacks = models.IntegerField()
    repositories = models.IntegerField()
    pinned_repositories = models.IntegerField()
    has_five_or_more_stacks = models.BooleanField()
    has_ten_or_more_stacks = models.BooleanField()
    has_five_or_more_repos = models.BooleanField()
    has_ten_or_more_repos = models.BooleanField()
    has_two_or_more_pinned = models.BooleanField()
    has_four_or_more_pinned = models.BooleanField()
    grade = models.IntegerField()
    github_profile_image = models.ImageField()

    def __str__(self):
        return f"{self.github_user}: {self.grade}/100"


class GroupCSV(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField()

    def __str__(self):
        return str(self.file)


class GroupEvaluation(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    csv_file = models.ForeignKey(GroupCSV, on_delete=models.CASCADE)
    github_user = models.CharField(max_length=50)
    evaluation_date = models.DateField(auto_now_add=True)
    has_profile_readme = models.BooleanField(default=True)
    has_photo = models.BooleanField()
    has_email = models.BooleanField()
    has_linkedin = models.BooleanField()
    stacks = models.IntegerField()
    repositories = models.IntegerField()
    pinned_repositories = models.IntegerField()
    has_five_or_more_stacks = models.BooleanField()
    has_ten_or_more_stacks = models.BooleanField()
    has_five_or_more_repos = models.BooleanField()
    has_ten_or_more_repos = models.BooleanField()
    has_two_or_more_pinned = models.BooleanField()
    has_four_or_more_pinned = models.BooleanField()
    grade = models.IntegerField()
    github_profile_image = models.ImageField()

    def __str__(self):
        return f"{self.github_user}: {self.grade}/100"


class MedianGrade(models.Model):
    median_grade = models.IntegerField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
