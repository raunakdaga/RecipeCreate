import urllib
import urllib2
import webbrowser

data = urllib.urlencode({'q': 'egg, spinach'})
url = 'https://recipeland.com/recipes/ingredients/search'
full_url = url + '?' + data
response = urllib2.urlopen(full_url)
with open("results.html", "w") as f:
    f.write(response.read())

webbrowser.open("results.html")
