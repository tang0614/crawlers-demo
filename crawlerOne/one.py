import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from RegexParser import *
import sys
import numpy as np

#Initialize browser
my_parser = RegexParser() 
f=open("tt.txt","w")
driver = webdriver.Chrome(ChromeDriverManager().install())




def main(lower_bound):

	geneDic={}

	for screen_id in range(lower_bound,lower_bound+10):
		screen_dic = {}
		#print (driver.page_source,file=f)
		try:
			driver.get(f'https://orcs.thebiogrid.org/Screen/{screen_id}')
			time.sleep(2) # Let the user actually see something!

			block_matches = my_parser.parse("Gene\/\d*?\" (title=\".*?\">.*?<\/a>.*?)maxRank",driver.page_source)

			for match in block_matches:
				# print(match)
				gene_match = my_parser.parse("title=\"(.*?)\">.*?<\/a>",match)
				alias_match = my_parser.parse("class=\" text-left hidden-sm hidden-xs\">(.*?)<\/td>" ,match)
				score1_match = my_parser.parse("class=\"text-center sorting_2\">(.*?)<\/td>" ,match)
				rank_match = my_parser.parse("#<strong>([\d,]*?)<",match)
				hit_match = my_parser.parse("class=\"text-ratingF popupTextUnderline\">(.*?)<\/span>",match)



				screen_dic[gene_match[0]]= {'ALIASES':alias_match[0],
									'SCORE.1':score1_match[0],
									'HIT':hit_match,
									'RANK':rank_match[0]}
									
				geneDic[screen_id]= screen_dic			
				print(geneDic)
				
		except Exception:
			continue
			



	np.save(f"/Users/xinyutang/Desktop/biogridData/DataPreprocessing/single_screen{lower_bound}.npy", geneDic)

	# input()



if __name__== "__main__":

	lower_bounds=sys.argv[1:]

	for num in lower_bounds:

		bound = int(num.strip(','))
		print(bound)
		main(bound)