from django.db import models

class Tracker(models.Model):
    name = models.CharField(max_length=25)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - clicks: {self.clicks}"

class Evaluation(models.Model):
    github_user = models.CharField(max_length=50)
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


    def __str__(self):
        return f'{self.github_user}: {self.grade}/100'
