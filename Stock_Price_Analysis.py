

# In[1]:


from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Data
# 
# We need to get data using pandas datareader. We will get stock information for the following banks:
# *  Bank of America
# * CitiGroup
# * Goldman Sachs
# * JPMorgan Chase
# * Morgan Stanley
# * Wells Fargo
# 
# ** Figure out how to get the stock data from Jan 1st 2006 to Jan 1st 2016 for each of these banks. Set each bank to be a separate dataframe, with the variable name for that bank being its ticker symbol. This will involve a few steps:**
# 1. Use datetime to set start and end datetime objects.
# 2. Figure out the ticker symbol for each bank.
# 3. Figure out how to use datareader to grab info on the stock.


# In[2]:


start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)


# In[3]:


bank_stocks = pd.read_pickle('all_banks')


# ** Check the head of the bank_stocks dataframe.**

# In[4]:


bank_stocks.head()


# In[5]:


tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']


# In[6]:


for tick in tickers:
    print(tick,bank_stocks[tick]['Close'].max())


# In[7]:


bank_stocks.xs(key='Close', axis=1, level='Stock Info').max()




# In[8]:


returns = pd.DataFrame()



# In[9]:


for tick in tickers:
    returns[tick + ' Return'] = bank_stocks[tick]['Close'].pct_change()

returns.head()



# In[10]:


import seaborn as sns
sns.pairplot(returns[1:])



# In[11]:


returns.idxmin()


# In[12]:


returns.idxmax()



# In[13]:


returns.std()


# In[14]:


returns.loc['2015-01-01':'2015-12-31'].std()


# ** Create a distplot using seaborn of the 2015 returns for Morgan Stanley **

# In[15]:


sns.distplot(returns.loc['2015-01-01':'2015-12-31']['MS Return'], color='green', bins=50)


# ** Create a distplot using seaborn of the 2008 returns for CitiGroup **

# In[16]:


sns.distplot(returns.loc['2008-01-01':'2008-12-31']['C Return'], color='red', bins=50)



# More Visualization



# In[17]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')

# Optional Plotly Method Imports
import plotly
import cufflinks as cf
cf.go_offline()


# Create a line plot showing Close price for each bank for the entire index of time.

# In[18]:


for tick in tickers:
    bank_stocks[tick]['Close'].plot(label=tick, figsize=(12,4))
plt.legend()


# In[19]:


bank_stocks.xs(key='Close', axis=1, level='Stock Info').plot()


# In[20]:


bank_stocks.xs(key='Close',axis=1,level='Stock Info').iplot()


# Moving Averages
# 
# The moving averages for these stocks in the year 2008. 
# 
# ** Plot the rolling 30 day average against the Close Price for Bank Of America's stock for the year 2008**

# In[21]:


plt.figure(figsize=(12,6))
bank_stocks['BAC']['Close'].loc['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg')
bank_stocks['BAC']['Close'].loc['2008-01-01':'2009-01-01'].plot(label='BAC CLOSE')
plt.legend()


# ** Create a heatmap of the correlation between the stocks Close Price.**

# In[22]:


sns.heatmap(bank_stocks.xs(key='Close', axis=1, level='Stock Info').corr(), annot=True)


# Use seaborn's clustermap to cluster the correlations together:**

# In[23]:


sns.clustermap(bank_stocks.xs(key='Close', axis=1, level='Stock Info').corr(), annot=True)



# ** Use .iplot(kind='candle) to create a candle plot of Bank of America's stock from Jan 1st 2015 to Jan 1st 2016.**

# In[24]:


bank_stocks['BAC'][['Open', 'High', 'Low', 'Close']].loc['2015-01-01':'2016-01-01'].iplot(kind='candle')


# ** Use .ta_plot(study='sma') to create a Simple Moving Averages plot of Morgan Stanley for the year 2015.**

# In[25]:


bank_stocks['MS']['Close'].loc['2015-01-01':'2016-01-01'].ta_plot(study='sma',periods=[13,21,55],title='Simple Moving Averages')


# **Use .ta_plot(study='boll') to create a Bollinger Band Plot for Bank of America for the year 2015.**

# In[26]:


bank_stocks['BAC']['Close'].loc['2015-01-01':'2016-01-01'].ta_plot(study='boll')


