def get_readme(selector):
    if selector == 404:
        return None
    readme = selector.css("article.markdown-body").get()
    return readme


def get_tags(selector):

    stacks = [
        "html", "css", "javascript", "jest", "react", "cypress",
        "rtl", "react-testing-library", "redux", "docker", "sql",
        "mongo", "node", "express", "mocha", "next.js", "typescript",
        "jwt", "python", "csharp", "cpp", "postman", "nginx", "django",
        "bash", "sequelize", "prisma", "bootstrap", "linux", "mac", 
        "tailwind"
    ]

    if selector == 404:
        return 0
    
    stack_counter = 0

    for stack in stacks:
        for img in selector.css("img").getall():
            if stack in img:
                stack_counter += 1
                break
    
    return stack_counter
