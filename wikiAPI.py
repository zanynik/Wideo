import requests
import urllib.request
import wikipedia
import html2text
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from textblob import TextBlob
import string

def imgsave(page):
    for words in page.split(" "):
        if words in img:
            if img[-3:] == "jpg":
                urllib.request.urlretrieve(img, page + ".jpg")
                print("Got image")
                return True

def firstImg(page):
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "parse",
        "page": page,
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    for lines in DATA["parse"]["text"]["*"].split("File:",2)[1:]:
        if lines.split(".jpg",1)[1]:
            imgname = lines.split(".jpg",1)[0]
            break
    return imgname


wikiPage = wikipedia.page("Albert Einstein")

text = wikiPage.content.split("references",1)[0]
content = text.translate(str.maketrans('', '', string.punctuation))
blob = TextBlob(content)
noun_set = set(blob.noun_phrases)

for noun in noun_set:
    try:
        searchPage = wikipedia.search(noun)[0]
        name = firstImg(searchPage)
        print("img name ",name)
        for img in wikipedia.page(searchPage).images:
            print("img : ", img)
            if name in img:
                urllib.request.urlretrieve(img, searchPage + ".jpg")
                print("Got First image")
                break

    except Exception:
        pass


for link in wikiPage.links:
    imgname = firstImg(link)
    for img in wikipedia.page(link).images:
        if imgname in img:
            urllib.request.urlretrieve(img, link + ".jpg")
            print("Got Link image")
            break
