import requests
from core import config as cfg
import pandas as pd
import sys
import simplejson as json

def extractGenes(lower_bound,upper_bound):
    geneID_list=[str(x) for x in range(lower_bound,upper_bound)]

    request_url = cfg.BASE_URL + "/genes/"
    params = {
        "accesskey": cfg.ACCESS_KEY,
    #     "name": "ATG9A",
        "geneID": "|".join(geneID_list),
        #"organismID": "9606",
    #     "hit": "yes",
        "format": "json"
    }
    r = requests.get( request_url, params = params )

    genes = r.json( )
    print( "Number of Genes Found: " + str(len(genes)) )

    with open(f'/Users/xinyutang/Desktop/biogridData/genes{upper_bound}.json', 'w') as f:
        json.dump(genes, f)

def main():
    # print command line arguments
    lower_bounds=sys.argv[1:]

    for num in lower_bounds:

        try:
            lower_bound = int(num.strip(','))
            print(lower_bound)
            upper_bound=lower_bound+500
            print(upper_bound)
            extractGenes(lower_bound,upper_bound)
        except:
            pass

  
if __name__== "__main__":
    
    main()
   
    