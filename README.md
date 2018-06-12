# Yale Scrape

Below is an updated version of the initial code that should be able to fetch all articles
from Yale's website - however only if the programmatic access doesn't get blocked.

Check out 'scrape.py' for a more general, working solution with explanations and tasks :)

```
import newspaper
from newspaper import Article


yale_paper = newspaper.build('http://www.yale.edu')

for article in yale_paper.articles:
	try:
		print(article.url)
		current_article = Article(url=article.url)
		current_article.download()
		current_article.parse()
		filename = article.url.split("/")[-1]
		with open(f"{filename}.txt", 'w') as f:
			f.write(current_article.text)
	except:
		continue
```


## Possible restricted access

I assume that it is not working due to some restrictions, because, reducing the code to its very basic form:

```
yp = Article(url='http://www.yale.edu')
yp.download()
yp.parse()
print(yp.text)
```

I received the following text as a result (which would clearly not contain further links):

	It looks like you're trying to zoom in on this page.
	For best results: use the most recent version of your browser, 
	disable your browser's 'zoom text only' setting, and use your browser's default font size settings.

	To zoom in, use [Ctrl] + [+] in Windows, and [Cmd] + [+] on a Mac. 
	To zoom out, use the keyboard shortcut [Ctrl] + [-] in Windows and [Cmd] + [-] on a Mac.

