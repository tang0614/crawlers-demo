import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from RegexParser import *
import sys
import pandas as pd
from bs4 import BeautifulSoup
import re
import numpy as np


#Initialize browser
my_parser = RegexParser() 
f=open("tt.txt","w")
driver = webdriver.Chrome(ChromeDriverManager().install())



def main(parameter,screenDic):
	#Open the URL
	driver.get(f'https://orcs.thebiogrid.org/Screen/{parameter}')
	time.sleep(2) # Let the user actually see something!


	content = driver.page_source
	soup = BeautifulSoup(content) # getting the html content of this url

	info={}
	info['SCREENID']=parameter

	for i in soup.findAll('div',attrs={'class':'col-lg-12 col-md-12 col-sm-12 col-xs-12'}):
		count =0

		for ul in i.findAll('ul',attrs={'class':'marginBotNone marginTopNone'}):
		   
		
			for li in ul.findAll('li'):
				
				first_split= re.split('/n', li.text.replace("|",'/n'))

				for element in first_split:
					
					try:
						title, ans = element.split(':')
						info[title]=ans

					except Exception:
						info['Notes']=element	
		
	screenDic[num] = info


if __name__== "__main__":

	lower_bounds=sys.argv[1:]
	screenDic={}

	for num in lower_bounds:

		num = int(num.strip(','))
		main(num,screenDic)

	np.save(f"/Users/xinyutang/Desktop/biogridData/DataPreprocessing/screens{num}.npy", screenDic)

	# note = a.find('li')
	# print(note)
	# notes.append(note)



# Find section by id: soup.find(id='ResultsContainer')
# .find_all() on a Beautiful Soup object, which returns an iterable containing all the HTML for all the job listings displayed on that page.
# Find by section .find_all('section', class_='card-content')
# Find by string. .find_all('h2', string='Python Developer')
# Find by a tag, .find_all('a')
# .find_all('h2', string=lambda text: 'python' in text.lower())
# .text to a Beautiful Soup object to return only the text content of the HTML elements that the object contains
# .contents, which will return the tag’s children as a Python list data type.
# if None in (title_elem, company_elem, location_elem): continue