from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen


def testParser(url):
    content = urlopen(url).read().decode()
    parser = ImgParser()
    parser.feed(content)
    return parser.getImages()

class ImgParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    self.images.append(attr[1])
            

    def getImages(self):
        return self.images
