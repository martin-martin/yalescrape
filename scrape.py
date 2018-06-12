import newspaper
from newspaper import Article


linklist = []
# 'links.txt' is copy-pasted from the 1st time running 'yalescrape.py', when it gave URLs as results
with open('links.txt', 'r') as f:
	for link in f.readlines():
		link = link.rstrip()
		linklist.append(link)

failcount = 0
for url in linklist:
	# the script failed and exited sometimes (again, probably due to some restrictions),
	# so I wrapped it into a try-except block to keep it going also if it hits a problem
	# NOTE: good Exception handling is an important part of coding, and this is only
	# 		a quick fix, nothing fancy!
	try:
		# this is basically the code you were using
		article = Article(url=url)
		article.download()
		article.parse()
		# here I am adding a way to name the files that are created
		# --TASK--: can you figure out how this code works? :)
		#			play around and check out the documentation for str.split()
		filename = url.split("/")[-1]
		# this is a common pattern to open a file and write to it
		# --TASK--: try extracting from the three examples down below:
		# 			- how the most basic code structure for this looks like
		#			- what the different letters ('w', 'a') mean
		with open(f"articles/{filename}.txt", 'w') as f:
			f.write(article.text)
	# if there are any troubles in the code above, the 'except' block gets called
	# --TASK--: what does it do?
	except Exception as e:
		with open('failcount.txt', 'a') as f:
			f.write(f"{e} : {url}\n")
		failcount += 1

# --TASK--: why is this code not indented? what is its aim?
with open('failcount.txt', 'a') as f:
	f.write(f"\n {failcount} TOTAL ERRORS")
