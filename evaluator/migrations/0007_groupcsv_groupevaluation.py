# Generated by Django 4.1 on 2022-09-10 22:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("evaluator", "0006_remove_evaluation_id_evaluation_uuid"),
    ]

    operations = [
        migrations.CreateModel(
            name="GroupCSV",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("file", models.FileField(upload_to="evaluator/static/csvs")),
            ],
        ),
        migrations.CreateModel(
            name="GroupEvaluation",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("github_user", models.CharField(max_length=50)),
                ("evaluation_date", models.DateField(auto_now_add=True)),
                ("has_photo", models.BooleanField()),
                ("has_email", models.BooleanField()),
                ("has_linkedin", models.BooleanField()),
                ("stacks", models.IntegerField()),
                ("repositories", models.IntegerField()),
                ("pinned_repositories", models.IntegerField()),
                ("has_five_or_more_stacks", models.BooleanField()),
                ("has_ten_or_more_stacks", models.BooleanField()),
                ("has_five_or_more_repos", models.BooleanField()),
                ("has_ten_or_more_repos", models.BooleanField()),
                ("has_two_or_more_pinned", models.BooleanField()),
                ("has_four_or_more_pinned", models.BooleanField()),
                ("grade", models.IntegerField()),
                ("github_profile_image", models.ImageField(upload_to="")),
                (
                    "csv_file",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="evaluator.groupcsv",
                    ),
                ),
            ],
        ),
    ]
