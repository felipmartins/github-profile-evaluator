from .models import Evaluation, GroupEvaluation


def new_evaluation(user_dic):

    new_eval = Evaluation(
        github_user=user_dic["github_username"],
        has_profile_readme=True if user_dic["readme"] else False,
        has_photo=user_dic["photo"],
        has_email=user_dic["email"],
        has_linkedin=user_dic["linkedin"],
        stacks=user_dic["tags"],
        repositories=user_dic["repos"],
        pinned_repositories=user_dic["pinned"],
        has_five_or_more_stacks=user_dic["has_five_tags"],
        has_ten_or_more_stacks=user_dic["has_ten_tags"],
        has_five_or_more_repos=user_dic["has_five_repos"],
        has_ten_or_more_repos=user_dic["has_ten_repos"],
        has_two_or_more_pinned=user_dic["has_two_pinned"],
        has_four_or_more_pinned=user_dic["has_four_pinned"],
        grade=user_dic["grade"],
        github_profile_image=user_dic["github_username"] + "_image.jpg",
    )

    new_eval.save()

    return new_eval


def new_group_evaluation(list_of_dicts, group_csv):

    for user_dic in list_of_dicts:

        new_eval = GroupEvaluation(
            csv_file=group_csv,
            github_user=user_dic["github_username"],
            has_profile_readme=True if user_dic["readme"] else False,
            has_photo=user_dic["photo"],
            has_email=user_dic["email"],
            has_linkedin=user_dic["linkedin"],
            stacks=user_dic["tags"],
            repositories=user_dic["repos"],
            pinned_repositories=user_dic["pinned"],
            has_five_or_more_stacks=user_dic["has_five_tags"],
            has_ten_or_more_stacks=user_dic["has_ten_tags"],
            has_five_or_more_repos=user_dic["has_five_repos"],
            has_ten_or_more_repos=user_dic["has_ten_repos"],
            has_two_or_more_pinned=user_dic["has_two_pinned"],
            has_four_or_more_pinned=user_dic["has_four_pinned"],
            grade=user_dic["grade"],
            github_profile_image=user_dic["github_username"] + "_image.jpg",
        )

        new_eval.save()
