import requests
from time import sleep
from parsel import Selector
from .face_detection import FaceDetector


def single_fetch_content(github_user: str) -> dict:

    user_dict = dict()
    user_dict["github_username"] = github_user

    gh_profile_url = "https://github.com/" + github_user
    git_response = requests.get(gh_profile_url)
    user_dict["github"] = (
        Selector(text=git_response.text) if git_response.status_code == 200 else None
    )

    readme_response = requests.get(gh_profile_url + "/" + github_user)

    user_dict["github_readme"] = (
        Selector(text=readme_response.text)
        if readme_response.status_code == 200
        else None
    )

    if not user_dict["github"]:
        photo_url = "https://i.imgur.com/PRiA9r9.png"
    else:
        photo_url = user_dict["github"].css('a[itemprop="image"]::attr(href)').get()

    photo_response = requests.get(photo_url)

    gh_image_path = "media/" + github_user + "_image.jpg"
    with open(gh_image_path, "wb") as handler:
        handler.write(photo_response.content)
        user_dict["photo"] = FaceDetector.find_faces(gh_image_path)

    return user_dict


def many_fetch_content(list_of_dicts: list) -> list:

    fetch_group = []

    for each_dict in list_of_dicts:
        fetch_group.append(single_fetch_content(each_dict["github_username"]))
        sleep(0.5)

    return fetch_group
