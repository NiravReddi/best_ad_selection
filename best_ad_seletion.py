# -*- coding: utf-8 -*-
"""Best_ad_seletion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hKkAV3b5-PYANIRFLCT9rMuyzx8u2H0G
"""



"""# importing datasets"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math

"""# Getting datasets"""

dataset = pd.read_csv("ADS_CT~1.CSV")

print(dataset)

"""# UPC algorithm"""

N=10000
d=10
ads_selected=[]
number_of_selections = [0] * d
sum_of_rewards = [0] * d
total_reward=0
for i in range(0,N):
  ad=0
  max_upper_bound = 0
  for j in range(1,d):
    if number_of_selections[j]>0 :
      avreage_reward = sum_of_rewards[j] / number_of_selections[j]
      delta_j = math.sqrt( ((3* math.log(i)/(2*math.log(j+1)))))
      upper_bound = avreage_reward + delta_j
    else:
      upper_bound = 1e400
    if(upper_bound > max_upper_bound ):
      max_upper_bound = upper_bound
      ad=j
  ads_selected.append(ad)
  number_of_selections[ad]+=1
  reward = dataset.values[i,ad]
  sum_of_rewards[ad] += avreage_reward
  total_reward += reward

print(ads_selected)

"""# Visualization"""

plt.hist(ads_selected)
plt.show()