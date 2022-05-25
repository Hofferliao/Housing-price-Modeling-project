#!/usr/bin/env python
# coding: utf-8

# In[67]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('pylab', 'inline')
pylab.rcParams['figure.figsize'] = (15.0, 12.0)

test = pd.read_csv('/Users/hofferliao/Downloads/house-prices-advanced-regression-techniques/test.csv')
train =pd.read_csv('/Users/hofferliao/Downloads/house-prices-advanced-regression-techniques/train.csv')


# In[68]:


train['SalePrice'].describe()


# In[69]:


train[train['SalePrice']>500000]


# In[70]:


train.head()


# In[81]:


# set ID as the index of the data frame.
train = train.set_index('Id')


# In[82]:


train.head()


# In[83]:


train.index.names =[None]


# In[85]:


train.head()


# In[86]:


train.describe()


# In[76]:





# In[88]:


plt.figure()
plt.scatter(train['GrLivArea'],train['SalePrice'])


# In[ ]:


#


# In[78]:


train.corr()


# In[79]:


sns.heatmap(train.corr())


# In[92]:


train[train.duplicated()] # ensure no duplicated line.


# In[98]:


test.head()


# In[101]:


test.index.names=[None]
test.describe()


# In[ ]:


#remove redudant variances
# extremly corelated to other variances. pick one 'square footage' ones, pick the one has higest corr. 
# amazon BI path

