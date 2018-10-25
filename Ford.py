import urllib
from urllib import urlopen
url="https://www.swarovski.com"
html=urlopen(url).read()
import nltk
raw=nltk.clean_html(html)
html[:1000]

import re
raw1=re.sub(r'[^\x00-\x7f]',r'',raw)
raw2=raw1.replace(".","")
raw3=raw2.replace(",","")
raw4=raw3.replace("&","")
raw5=raw4.replace("1-200000","")
tokens=nltk.word_tokenize(raw5)
stopwords=nltk.corpus.stopwords.words('english')
tokens1=[w for w in tokens if w.lower() not in stopwords]
from nltk import FreqDist
fdist2=FreqDist(tokens1)
fdist2.plot(50,cumulative=True)



