import numpy as np
from read_text import read_text
from model import summary_model

def get_summary(link, from_file = False, ratio = 0.02, max_size = 5000):
	"""
	returns summary of either a 
	local text file	or a webpage
	"""
	text = read_text(link, from_file)
	result = summary_model(text, ratio, max_size)
	return result