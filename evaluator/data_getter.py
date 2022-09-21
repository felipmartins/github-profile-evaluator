from evaluator.profile_handler import (
    get_pinned_repos,
    get_repos,
    has_email,
    has_linkedin,
    get_sidebar,
)
from evaluator.readme_handler import get_readme, get_tags


def populate_dict(user_dict):
    user_dict["readme"] = get_readme(user_dict["github_readme"])
    user_dict["sidebar"] = get_sidebar(user_dict["github"])
    user_dict["linkedin"] = has_linkedin(user_dict["sidebar"], user_dict["readme"])
    user_dict["email"] = has_email(user_dict["sidebar"], user_dict["readme"])
    user_dict["tags"] = get_tags(user_dict["github_readme"])
    user_dict["repos"] = get_repos(user_dict["github"])
    user_dict["pinned"] = get_pinned_repos(user_dict["github"])

    return user_dict


def populate_dicts(list_of_dicts):

    for index, each_dict in enumerate(list_of_dicts):
        populate_dict(each_dict)
        print(f"pessoa #{index} de {len(list_of_dicts)}")

    return list_of_dicts
