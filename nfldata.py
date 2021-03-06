
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np
from numpy.random import randn


# In[51]:


a = pd.read_csv("tracking_gameId_2017090700.csv")
a
b = pd.read_csv("players.csv")
c = pd.read_csv("games.csv")
b
#size = len(b.index)
b#['foo']=randn(size)
c.head()
c["gameId"]
a["gameId"]

#get the home team for gameId when same df.loc[df.set_of_numbers <= 4, 'equal_or_lower_than_4?'] = 'True'
d = pd.merge(a, c, on='gameId')
#[a['team'] == 'away', a['teamName']=c['visitorTeamAbbr']
a.loc[a['team'] == 'away' , 'teamName'] = c['visitorTeamAbbr']
a.loc[a['team'] == 'home', 'teamName'] = c['homeTeamAbbr']

def samePlayer(name1, name2):
    return name1==name2

