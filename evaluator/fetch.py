import requests
from time import sleep
from parsel import Selector
from .face_detection import FaceDetector


def single_fetch_content(github_user):
    git_url = "https://github.com/" + github_user
    readme_url = "https://github.com/" + github_user + "/" + github_user

    git_response = requests.get(git_url)
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

    with open("evaluator/media/" + github_user + "_image.jpg", "wb") as handler:
        handler.write(photo_response.content)
        user_dic["photo"] = FaceDetector.find_faces(
            "evaluator/media/" + github_user + "_image.jpg"
        )

    return user_dic


def many_fetch_content(list_of_dicts):

    general_list_of_dicts = []

    for each_dict in list_of_dicts:
        general_list_of_dicts.append(single_fetch_content(each_dict["github_username"]))

    return general_list_of_dicts
