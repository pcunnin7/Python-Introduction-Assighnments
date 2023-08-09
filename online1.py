from urllib.request import urlopen

url = 'www.google.com'
response = urlopen('http://www.depaul.edu')
html = response.read()
html = str(html)
content = str(urlopen(url).read())
from html.parser import HTMLParser
parser = HTMLParser()
parser.feed(content)


from urllib.request import Request, urlopen
req = Request('https://www.cdm.depaul.edu')

