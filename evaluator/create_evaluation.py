from .models import Evaluation

def new_evaluation(user_dic):

    new_eval = Evaluation(
        github_user = user_dic['github_username'],
        has_photo = user_dic["photo"],
        has_email = user_dic["email"],
        has_linkedin = user_dic["linkedin"],
        stacks = user_dic["tags"],
        repositories = user_dic["repos"],
        pinned_repositories = user_dic["pinned"],
        has_five_or_more_stacks = user_dic["has_five_tags"] ,
        has_ten_or_more_stacks = user_dic["has_ten_tags"]  ,
        has_five_or_more_repos = user_dic["has_five_repos"],
        has_ten_or_more_repos = user_dic["has_ten_repos"] ,
        has_two_or_more_pinned = user_dic["has_two_pinned"],
        has_four_or_more_pinned = user_dic["has_four_pinned"],
        grade = user_dic['grade']
    )

    new_eval.save()

