python
import urllib
from urllib import urlopen
url="http://www.foxnews.com"
html=urlopen(url).read()
import nltk
raw=nltk.clean_html(html)
html[:1000]

 
import re
raw1=re.sub(r'[^\x00-\x7f]',r'',raw)
raw2=raw1.replace(";","")
 raw3=raw2.replace(":","")
raw4=raw3.replace("'","")
raw5=raw4.replace(",","")
raw6=raw5.replace("?","")
raw7=raw6.replace("&","")
raw8=raw7.replace("#","")
raw9=raw8.replace("+","")
raw10=raw9.replace("-","")
raw11=raw10.replace(".","")
raw12=raw11.replace("'s","")
raw13=raw12.replace("23","")
raw14=raw13.replace("3","")
raw15=raw14.replace("4","")
tokens=nltk.word_tokenize(raw15)
stopwords=nltk.corpus.stopwords.words('english')
tokens1=[w for w in tokens if w.lower() not in stopwords]
from nltk import FreqDist
fdist2=FreqDist(tokens1)
fdist2.plot(50,cumulative=True)
