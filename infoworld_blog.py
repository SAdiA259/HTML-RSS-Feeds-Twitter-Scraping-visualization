python
import feedparser
d=feedparser.parse('https://www.infoworld.com/blog/cloud-computing/index.rss')
print d['feed']['title']
InfoWorld Cloud Computing
print d['feed']['link']
https://www.infoworld.com
import nltk
for post in d.entries:
...     print post.title
import feedparser
import re
import nltk
from nltk import FreqDist
d=feedparser.parse('https://www.infoworld.com/blog/cloud-computing/index.rss')
raw=""
for post in d.entries:
...     temp=re.sub(r'[^\x00-\x7f]',r"",post.title)
...     temp1=temp.replace("'","")
...     temp2=temp1.replace(",","")
...     temp3=temp2.replace(":","")
...     temp4=temp3.replace("?","")
...     raw=raw+str(temp4)
... 
tokens=nltk.word_tokenize(raw)
stopwords=nltk.corpus.stopwords.words('english')
tokens1=[w for w in tokens if w.lower() not in stopwords]
fdist2=FreqDist(tokens1)
fdist2.plot(50,cumulative=True)
