from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("evaluator", "0009_alter_groupcsv_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="groupcsv",
            name="file",
            field=models.FileField(upload_to="evaluator/media/csvs/"),
        ),
    ]
