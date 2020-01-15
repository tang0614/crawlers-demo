import requests
from core import config as cfg
import pandas as pd
import sys
import simplejson as json
import pickle
import numpy as np
import os

"""
Fetch screen annotation with customizable search criteria
that can be tailored to match your own requirements. Then fetch 
the score values associated with those screens.
"""



request_url = cfg.BASE_URL + "/screens/"

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
# In this example, we've chosen to only receive toxin exposure and virus exposure experiments
# and also to limit to only human results.
screenID_list=[str(x) for x in range(2000)]

params = {
"accesskey": cfg.ACCESS_KEY,
"screenID": "|".join(screenID_list),
"format": "json"
}

r = requests.get( request_url, params = params )
screens = r.json( )
print( "Number of Screens Found: " + str(len(screens)) )
print(screens)

# Step through each matching screen, and make a request
# for the associated score data
scores = {}

for screen in screens :
	request_url = cfg.BASE_URL + "/screen/" + str(screen['SCREEN_ID'])

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
# if you are not interested in a full set of score data. In this case, we only want scores
# marked as hits.
params = {
    "accesskey": cfg.ACCESS_KEY,
    "format": "json",
    "hit": "yes"
}

r = requests.get( request_url, params = params )
score_set = r.json( )

# Convert the returned score_set into an indexed one 
# where you can retrieve rows by IDENTIFIER_ID
indexed_scores = {}
for row in score_set :
    indexed_scores[row['IDENTIFIER_ID']] = row

scores[str(screen['SCREEN_ID'])] = indexed_scores


np.save('scores',scores) 



# Print Results for the same gene (AACS) from each screen
# If it's in the associated list of hits
# 	for screen_id, score_set in scores.items( ) :
# 	    if '79065' in score_set :
# 	        print( score_set['79065'] )

# 	print( "Number of Score Sets: " + str(len(scores)) )








