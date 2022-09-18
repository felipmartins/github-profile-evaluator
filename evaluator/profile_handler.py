def get_image_url(selector):
    try:
        return selector.css('a[itemprop="image"]::attr(href)').get()
    except AttributeError:
        return None


def get_sidebar(selector):
    try:
        return selector.css("div.js-profile-editable-area").get()
    except AttributeError:
        return None


def get_repos(selector):
    try:
        repo = selector.css("span.Counter::text").get()
    except AttributeError:
        return None
    return int(repo) if repo else 0


def get_pinned_repos(selector):
    try:
        check_pinned = selector.css("h2.f4.mb-2.text-normal::text").get()
    except AttributeError:
        return None

    if not check_pinned or "Pinned" not in check_pinned:
        return 0

    return len(selector.css("div.Box.d-flex.pinned-item-list-item").getall())


def has_email(sidebar, readme):
    providers = [
        "@gmail.com",
        "@hotmail.com",
        "@outlook.com",
        "@yahoo.com",
        "@yahoo.com.br",
        "@terra.com.br",
        "@live.com",
        "@icloud.com",
    ]

    if sidebar is None and readme is None:
        return False
    elif sidebar is None and readme is not None:
        return any([email in readme.lower() for email in providers])
    elif sidebar is not None and readme is None:
        return any([email in sidebar.lower() for email in providers])

    return any([email in readme.lower() for email in providers]) or any(
        [email in sidebar.lower() for email in providers]
    )


def has_linkedin(sidebar, readme):
    in_readme = "linkedin.com/in" in readme.lower() if readme else False
    in_sidebar = "linkedin.com/in" in sidebar.lower() if sidebar else False

    return in_sidebar or in_readme
