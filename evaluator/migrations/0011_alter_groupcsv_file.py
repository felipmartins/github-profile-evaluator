# Generated by Django 4.1.1 on 2022-09-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("evaluator", "0010_alter_groupcsv_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="groupcsv",
            name="file",
            field=models.FileField(upload_to=""),
        ),
    ]
