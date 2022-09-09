def get_image_url(selector):
    if selector == 404:
        return None
    image_url = selector.css('a[itemprop="image"]::attr(href)').get()
    return image_url


def get_sidebar(selector):
    if selector == 404:
        return None
    sidebar = selector.css("div.Layout-sidebar").get()
    return sidebar


def get_repos(selector):
    if selector == 404:
        return None
    repo = selector.css("span.Counter::text").get()
    if repo:
        return int(repo)
    else:
        return 0


def get_pinned_repos(selector):
    if selector == 404:
        return None
    check_pinned = selector.css("h2.f4.mb-2.text-normal::text").get()
    if check_pinned:
        if "Pinned" in check_pinned:
            repo = selector.css("div.Box.d-flex.pinned-item-list-item").getall()
        else:
            repo = []
    else:
        repo = []
    return len(repo)


def has_email(sidebar, readme):
    providers = [
                 "@gmail.com", "@hotmail.com", 
                 "@outlook.com", "@yahoo.com", 
                 "@yahoo.com.br", "@terra.com.br",
                 "@live.com", "@icloud.com"
                 ]

    if sidebar is None and readme is None:
        return False
    elif sidebar is None and readme is not None:
        return any([email in readme.lower() for email in providers])
    elif sidebar is not None and readme is None:
        return any([email in sidebar.lower() for email in providers])

    return any([email in readme.lower() for email in providers]) or any([email in sidebar.lower() for email in providers])


def has_linkedin(sidebar, readme):
    if sidebar is None and readme is None:
        return False
    elif sidebar is None and readme is not None:
        return "linkedin.com/in" in readme.lower()
    elif sidebar is not None and readme is None:
        return "linkedin.com/in" in sidebar.lower()

    return "linkedin.com/in" in readme.lower() or "linkedin.com/in" in sidebar.lower()
