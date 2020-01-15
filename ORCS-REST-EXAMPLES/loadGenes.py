import requests
from core import config as cfg
import pandas as pd
import numpy as np
import sys
import time
from tqdm import tqdm
import os



def main():
    # print command line arguments
    parameter=sys.argv[1:][0]
    directory = f'/Users/xinyutang/Desktop/biogridData/{parameter}/'

    genes_list=[]

    for file in tqdm(os.listdir(directory)):
        time.sleep(3)
        filename = os.fsdecode(file)


        if filename.startswith("gene"): 
            path = os.path.join(directory, filename)
            genes =pd.read_json (path)
            
            try:
                df = genes[['SCREEN_ID','IDENTIFIER_ID','OFFICIAL_SYMBOL','SCORE.1','SCORE.2','ALIASES','HIT']]
                df = df.sort_values('SCREEN_ID',ascending='True')
                genes_list.append(df)
            
            except Exception:
                pass

        else:
            continue
            
    allgenes = pd.concat(genes_list,axis=0)
    allgenes = allgenes.sort_values('SCREEN_ID').reset_index(drop=True)
    allgenes.to_pickle(f'/Users/xinyutang/Desktop/biogridData/DataPreprocessing/allGenes_{parameter}.pkl')




if __name__== "__main__":
    
    main()