# NOTE: this is the initial code. works to deliver a list of links when run the first time
# 		Yale might be blocking programmatic access, afterwards I only get the first link

import newspaper
from newspaper import Article

yale_paper = newspaper.build('http://www.yale.edu')

for article in yale_paper.articles:
    print(article.url)

#this returns a list of urls that are called and each url is a separate article. I took the first two urls and extracted the articles from them.
#The challenge is how to get download and parse the urls without having to cut and paste
#I tried a couple of for loops but they aren’t quite right
    
lista = ['http://news.yale.edu/2012/10/11/nearby-super-earth-likely-diamond-planet','http://news.yale.edu/2012/10/31/exhaustive-family-tree-birds-shows-recent-rapid-diversification' ]
for list in lista:

   first_article = Article(url="%s" % list)

   first_article.download()

   first_article.parse()

   print(first_article.text)


'''
--------------------------------------------------------------------------------------------
Below is an updated version of the code above that should be able to fetch all articles
from the Yale website - if the programmatic access doesn't get blocked.

Check out 'scrape.py' for a more general, working solution with explanations and tasks :)
--------------------------------------------------------------------------------------------
'''

# yale_paper = newspaper.build('http://www.yale.edu')

# for article in yale_paper.articles:
# 	try:
# 		print(article.url)
# 		current_article = Article(url=article.url)
# 		current_article.download()
# 		current_article.parse()
# 		filename = article.url.split("/")[-1]
# 		with open(f"{filename}.txt", 'w') as f:
# 			f.write(current_article.text)
# 	except:
# 		continue



'''
-- I assume that it is not working due to some restrictions, because, reducing it to the very basic: --

yp = Article(url='http://www.yale.edu')
yp.download()
yp.parse()
print(yp.text)

-- I received the following text as a result (which would not contain further links): --

It looks like you're trying to zoom in on this page.
For best results: use the most recent version of your browser, 
disable your browser's 'zoom text only' setting, and use your browser's default font size settings.

To zoom in, use [Ctrl] + [+] in Windows, and [Cmd] + [+] on a Mac. 
To zoom out, use the keyboard shortcut [Ctrl] + [-] in Windows and [Cmd] + [-] on a Mac.
'''
