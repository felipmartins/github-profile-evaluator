def get_readme(selector):
    if not selector:
        return None
    readme = selector.css("article.markdown-body").get()
    return readme


def get_tags(selector):

    if not selector:
        return 0

    stacks = [
        "html", "css", "javascript", "jest", "react", "cypress",
        "rtl", "react-testing-library", "redux", "docker", "sql",
        "mongo", "node", "express", "mocha", "next.js", "typescript",
        "jwt", "py", "csharp", "cpp", "postman", "nginx", "django",
        "bash", "sequelize", "prisma", "bootstrap", "linux", "mac",
        "tailwind", "algoritmos", "dados", "redes", "objetos", "js"
    ]

    stack_counter = 0

    for stack in stacks:
        if stack in selector.get().lower():
            stack_counter += 1

    return stack_counter
