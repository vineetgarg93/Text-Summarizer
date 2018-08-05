from bs4 import BeautifulSoup
from urllib.request import urlopen

def read_from_web(url):
	""" 
	return the title and the text of the article
	at the specified url
	"""
	page = urlopen(url)
	soup = BeautifulSoup(page, "lxml")
	text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
	return soup.title.text, text

def read_from_file(filename):
	"""
	return the text of the file
	at the specified location
	"""
	with open(filename, 'r') as myfile:
		text=myfile.read()
	return text

def read_text(link, from_file = False):
	"""
	reads text either from a
	local file location or a
	specifed webpage
	"""
	if from_file:
		text = read_from_file(link)
	else:
		_, text = read_from_web(link)

	return text