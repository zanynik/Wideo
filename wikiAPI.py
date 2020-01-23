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
import json

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

def linemerge(line):
    for i in range(len(line)):
        if len(line[i]) < 20 and i > 1:
            line[i-1:i+1] = [''.join(line[i-1:i+1])]
            #print(line[i-1])
            break
        if i == len(line) - 2:
            return
    linemerge(line)


wikiPage = wikipedia.page("Elinor Ostrom")

text = wikiPage.content.split("references",1)[0]
eachline = text.split(".")
linemerge(eachline)
refpages =[]
dict_js = {}
for i in range(len(eachline)):
    content = eachline[i].translate(str.maketrans('', '', string.punctuation))
    blob = TextBlob(content)
    nouns = blob.noun_phrases
    images=[]
    for noun in nouns:
        pageset = set(refpages)
        try:
            searchPage = wikipedia.search(noun)[0]
            print(noun,"page :",searchPage)
            name,ext = firstImg(searchPage)
            print("img name ",name)
            if name not in pageset:
                for img in wikipedia.page(searchPage).images:
                    print("img : ", img)
                    if name in img:
                        print("Here")
                        if ext == "jpg":
                            print("Here too")
                            images += [img]
                            print("Got JPG image")
                            break
                        if ext == "svg":
                            urllib.request.urlretrieve(img, "Elinor/"+ searchPage + ".svg")
                            print("Got SVG image")
                            break
            refpages.append(name)
            print(refpages)

        except Exception:
            pass
    dict_js[i] = {'imageurl': images, 'line': content}
    print(dict_js)
    if i == 10:
        with open("elinor.json", "w") as f:
            json.dump(dict_js, f)

        # To print out the JSON string (which you could then hardcode into the JS)
        json.dumps(dict_js)
        print("DONE")
        break

# for link in wikiPage.links:
#     imgname = firstImg(link)
#     for img in wikipedia.page(link).images:
#         if imgname in img:
#             urllib.request.urlretrieve(img, "Elinor/"+link + ".jpg")
#             print("Got Link image")
#             break
