import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.shortcuts import get_object_or_404
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle
from .models import Evaluation, GroupCSV, GroupEvaluation
from .tracker import raise_single_download_clicks, raise_group_download_clicks


def export_evaluations_csv():
    evaluations = Evaluation.objects.all()
    group_evaluations = GroupEvaluation.objects.all()

    with open("avaliacoes_github.csv", mode="w") as file:
        file.write(
            "github_username,has_profile_readme,has_photo,has_email,has_linkedin,number_of_stacks,number_of_repositories,number_of_pinned_repositories,has_five_stacks,has_ten_stacks,has_five_repos,has_ten_repos,has_two_pinned,has_four_pinned,grade\n"
        )
        for eval in evaluations:
            file.write(
                f"{eval.github_user},{eval.has_profile_readme},{eval.has_photo},{eval.has_email},{eval.has_linkedin},{eval.stacks},{eval.repositories},{eval.pinned_repositories},{eval.has_five_or_more_stacks},{eval.has_ten_or_more_stacks},{eval.has_five_or_more_repos},{eval.has_ten_or_more_repos},{eval.has_two_or_more_pinned},{eval.has_four_or_more_pinned},{eval.grade},\n"
            )

        for eval in group_evaluations:
            file.write(
                f"{eval.github_user},{eval.has_profile_readme},{eval.has_photo},{eval.has_email},{eval.has_linkedin},{eval.stacks},{eval.repositories},{eval.pinned_repositories},{eval.has_five_or_more_stacks},{eval.has_ten_or_more_stacks},{eval.has_five_or_more_repos},{eval.has_ten_or_more_repos},{eval.has_two_or_more_pinned},{eval.has_four_or_more_pinned},{eval.grade},\n"
            )


def export_list_evaluations_csv(csv_file):
    group_evaluations = GroupEvaluation.objects.all().filter(csv_file=csv_file)

    with open("avaliacoes_github.csv", mode="w") as file:
        file.write(
            "github_username,has_profile_readme,has_photo,has_email,has_linkedin,number_of_stacks,number_of_repositories,number_of_pinned_repositories,has_five_stacks,has_ten_stacks,has_five_repos,has_ten_repos,has_two_pinned,has_four_pinned,grade\n"
        )

        for eval in group_evaluations:
            file.write(
                f"{eval.github_user},{eval.has_profile_readme},{eval.has_photo},{eval.has_email},{eval.has_linkedin},{eval.stacks},{eval.repositories},{eval.pinned_repositories},{eval.has_five_or_more_stacks},{eval.has_ten_or_more_stacks},{eval.has_five_or_more_repos},{eval.has_ten_or_more_repos},{eval.has_two_or_more_pinned},{eval.has_four_or_more_pinned},{eval.grade},\n"
            )


def export_group_csv(uuid: str):
    
    csv_object = get_object_or_404(GroupCSV, uuid=uuid)
    filename = csv_object.file.path.split("/")[-1]
    evaluations = GroupEvaluation.objects.all().filter(csv_file=csv_object)

    with open('media/'+ filename, mode="w") as file:
        file.write(
            "github_username,has_profile_readme,has_photo,has_email,has_linkedin,number_of_stacks,number_of_repositories,number_of_pinned_repositories,has_five_stacks,has_ten_stacks,has_five_repos,has_ten_repos,has_two_pinned,has_four_pinned,grade\n"
        )

        for eval in evaluations:
            file.write(
                f"{eval.github_user},{eval.has_profile_readme},{eval.has_photo},{eval.has_email},{eval.has_linkedin},{eval.stacks},{eval.repositories},{eval.pinned_repositories},{eval.has_five_or_more_stacks},{eval.has_ten_or_more_stacks},{eval.has_five_or_more_repos},{eval.has_ten_or_more_repos},{eval.has_two_or_more_pinned},{eval.has_four_or_more_pinned},{eval.grade},\n"
            )

    
    return FileResponse(open('media/'+ filename, 'rb'), as_attachment=True, filename='avaliacao_'+filename)