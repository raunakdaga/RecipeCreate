import urllib
import getRecipeLink



def getHTML(ingredients):
    data = urllib.parse.urlencode({'q': getRecipeLink.getLink(ingredients)})
    url = 'https://recipeland.com/recipes/list?q='
    full_url = url + '?' + data
    response = urllib.request.urlopen(full_url)
    with open("results.html", "wb") as f:
        f.write(response.read())
