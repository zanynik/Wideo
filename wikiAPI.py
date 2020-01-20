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


wikiPage = wikipedia.page("Albert Einstein")

text = wikiPage.content.split("references",1)[0]
content = text.translate(str.maketrans('', '', string.punctuation))
blob = TextBlob(content)
noun_set = set(blob.noun_phrases)

for noun in noun_set:
    try:
        searchPage = wikipedia.search(noun)[0]
        for img in wikipedia.page(searchPage).images:
            page = searchPage
            if imgsave(page):
                break

    except Exception:
        pass


for link in wikiPage.links:
    for img in wikipedia.page(link).images:
        page = link
        if imgsave(page):
            break
