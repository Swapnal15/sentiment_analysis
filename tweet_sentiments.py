#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import pandas as pd
sentiment = pd.read_csv('tweets_analysis', delimiter = '\t')
tweet = sentiment['-1.0']

plt.hist(tweet, edgecolor='black', linewidth=1.2)
plt.xlabel('Sentiment Value')
plt.ylabel('Count')
plt.show()


# In[ ]:




