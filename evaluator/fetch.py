import requests
from time import sleep
from parsel import Selector
from .face_detection import FaceDetector


def single_fetch_content(github_user):
    GH_BASE_PATH = "https://github.com/"

    user_dict = dict()
    user_dict["github_username"] = github_user

    gh_profile_url = GH_BASE_PATH + github_user
    git_response = requests.get(gh_profile_url)
    user_dict["github"] = Selector(text=git_response.text)
    sleep(1)

    readme_url = gh_profile_url + "/" + github_user
    readme_response = requests.get(readme_url)
    sleep(1)

    if readme_response.status_code == 200:
        user_dict["github_readme"] = Selector(text=readme_response.text)
    else:
        user_dict["github_readme"] = None

    photo_url = (
        user_dict["github"].css('a[itemprop="image"]::attr(href)').get()
    )

    if not photo_url:
        photo_url = "https://i.imgur.com/PRiA9r9.png"

    photo_response = requests.get(photo_url)
    sleep(1)

    gh_image_path = "evaluator/media/" + github_user + "_image.jpg"
    with open(gh_image_path, "wb") as handler:
        handler.write(photo_response.content)
        user_dict["photo"] = FaceDetector.find_faces(gh_image_path)

    return user_dict


def many_fetch_content(list_of_dicts):

    general_list_of_dicts = []

    for each_dict in list_of_dicts:
        general_list_of_dicts.append(
            single_fetch_content(each_dict["github_username"])
        )

    return general_list_of_dicts
