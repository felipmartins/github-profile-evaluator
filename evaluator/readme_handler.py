def get_readme(selector):
    if selector == 404:
        return None
    readme = selector.css("article.markdown-body").get()
    return readme


def get_tags(selector):
    if selector == 404:
        return 0
    return len(selector.css("img").getall())
