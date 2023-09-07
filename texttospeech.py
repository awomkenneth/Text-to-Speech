#Import the libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os


#Get the article
article = Article('https://24naija.com/2023/07/26/must-see-photos-community-initiatives-to-promote-peace-host-media-practitioners-to-a-2-day-training/')
article.download()
article.parse()

nltk.download('punkt')
article.nlp()

#Get the articles text
mytext = article.text

language = "en"

myobj = gTTS(text=mytext, lang=language, slow=False)
print('jkdfjk')

myobj.save("newread_article.mp3")

os.system("open newread_article.mp3")
print('jkdfjk')


