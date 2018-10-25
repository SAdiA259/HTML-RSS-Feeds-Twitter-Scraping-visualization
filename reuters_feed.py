python
import feedparser
d=feedparser.parse('http://feeds.reuters.com/news/artsculture.rss')
print d['feed']['title']
Reuters: Arts
print d['feed']['link']
http://www.reuters.com
import nltk
for post in d.entries:
...     print post.title
... 
import feedparser
 import re
import nltk
from nltk import FreqDist
d=feedparser.parse('http://feeds.reuters.com/news/artsculture.rss')
raw=""
for post in d.entries:
...     temp=re.sub(r'[^\x00-\x7f]',r'',post.title)
...     temp1=temp.replace("'","")
...     temp2=temp1.replace(",","")
...     raw=raw+str(temp2)
tokens=nltk.word_tokenize(raw)
stopwords=nltk.corpus.stopwords.words('english')
tokens1=[w for w in tokens if w.lower() not in stopwords]
fdist2=FreqDist(tokens1)
fdist2.plot(50,cumulative=True)

