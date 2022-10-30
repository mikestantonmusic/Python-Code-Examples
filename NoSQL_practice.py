import os
import numpy as np
import json
import pandas as pd
import mytools.NoSQL_functions
from mytools.NoSQL_functions import *

def main():
   # get data from JSON file
   with open('data/Sample Json with 200 Records.json',encoding="utf-8") as f:
      data1 = json.load(f)

   # convert data to data frame and export to csv
   try:
      df = level2_json_df(data1, 'feeds', ['id','name'], 'multiMedia')
      df.to_csv('output/level2_json200_df.csv')
      print(df)
      print('data extraction successful')
   except:
      print('data extraction not successful')

if __name__ == "__main__":
   main()

