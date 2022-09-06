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
        grade = user_dic['grade']
    )

    new_eval.save()

