def getLink(ingredients):
    link = ''
    for ingredient in ingredients:
        link = link + ingredient + '+'
    link = link[:-1]
    return link
