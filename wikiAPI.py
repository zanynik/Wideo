import requests
import urllib.request
import urllib.parse
import wikipedia
import html
import html2text
# from nltk.corpus import stopwords
# from nltk.corpus import wordnet
from textblob import TextBlob
import string

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
            type = "jpg"
            imgname = lines.split(".jpg",1)[0]
            return urllib.parse.quote_plus(imgname), type
        if lines.split(".svg",1)[1]:
            type = "svg"
            imgname = lines.split(".svg",1)[0]
            return urllib.parse.quote_plus(imgname), type
        #Need to Encode the names

wikiPage = wikipedia.page("Elinor Ostrom")

text = wikiPage.content.split("references",1)[0]
content = text.translate(str.maketrans('', '', string.punctuation))
blob = TextBlob(content)
noun_set = set(blob.noun_phrases)
refpages =[]
for noun in noun_set:
    pageset = set(refpages)
    try:
        searchPage = wikipedia.search(noun)[0]
        name,ext = firstImg(searchPage)
        print("img name ",name)
        if name not in pageset:
            for img in wikipedia.page(searchPage).images:
                print("img : ", img)
                if name in img:
                    if ext == "jpg":
                        urllib.request.urlretrieve(img, "Elinor/"+ searchPage + ".jpg")
                        print("Got JPG image")
                        break
                    if ext == "svg":
                        urllib.request.urlretrieve(img, "Elinor/"+ searchPage + ".svg")
                        print("Got SVG image")
                        break
        refpages.append(name)

    except Exception:
        pass


for link in wikiPage.links:
    imgname = firstImg(link)
    for img in wikipedia.page(link).images:
        if imgname in img:
            urllib.request.urlretrieve(img, "Elinor/"+link + ".jpg")
            print("Got Link image")
            break
