import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from RegexParser import *


my_parser = RegexParser() 
f=open("tt.txt","w")
#Initialize browser
driver = webdriver.Chrome(ChromeDriverManager().install())


geneDic={}

for screen_id in range(800,1030):
	screen_dic = {}
	#print (driver.page_source,file=f)
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

	    



np.save("/Users/xinyutang/Desktop/biogridData/DataPreprocessing/single_screen3.npy", geneDic)

input()