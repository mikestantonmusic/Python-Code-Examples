import os
import numpy as np
import json
import pandas as pd
import NoSQL_functions
from NoSQL_functions import *

import os
os.chdir('JSON/')
print('current working directory:', os.getcwd())

import json

with open('data/Sample Json with 200 Records.json',encoding="utf-8") as f:
   data1 = json.load(f)

df = level2_json_df(data1, 'feeds', ['id','name'], 'multiMedia')
print(df.columns)
print(df)
