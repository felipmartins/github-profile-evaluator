import requests
from time import sleep
from parsel import Selector
from .face_detection import FaceDetector


def single_fetch_content(github_user):
    GH_BASE_PATH = "https://github.com/"
    gh_profile_url = GH_BASE_PATH + github_user
    readme_url = gh_profile_url + "/" + github_user

    git_response = requests.get(gh_profile_url)
    sleep(1)
    readme_response = requests.get(readme_url)
    sleep(1)

    user_dic = dict()

    user_dic["github_username"] = github_user

    user_dic["github"] = Selector(text=git_response.text)

    if readme_response.status_code == 200:
        user_dic["github_readme"] = Selector(text=readme_response.text)
    else:
        user_dic["github_readme"] = 404

    photo_url = user_dic["github"].css('a[itemprop="image"]::attr(href)').get()

    if not bool(photo_url):
        photo_url = "https://i.imgur.com/PRiA9r9.png"

    photo_response = requests.get(photo_url)
    sleep(1)

    gh_image_path = "evaluator/media/" + github_user + "_image.jpg"
    with open(gh_image_path, "wb") as handler:
        handler.write(photo_response.content)
        user_dic["photo"] = FaceDetector.find_faces(gh_image_path)

    return user_dic


def many_fetch_content(list_of_dicts):

    general_list_of_dicts = []

    for each_dict in list_of_dicts:
        general_list_of_dicts.append(
            single_fetch_content(each_dict["github_username"])
        )

    return general_list_of_dicts
