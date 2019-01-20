
# coding: utf-8

# In[32]:


# top 10 scorer


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


# In[33]:


xls = pd.ExcelFile('DataTales.xlsx')
test_scores = pd.read_excel(xls, 'Test scores')
test_master = pd.read_excel(xls, 'Test master')


# In[34]:


test  =test_scores[['Participant identifier', 'Test Name']]


# In[35]:


test_master = test_master[['Test name', 'Complexity']]


# In[36]:


easy = 0
medium = 0
difficult = 0

for index, row in test.iterrows():
    for i, r in test_master.iterrows():
        if(r['Test name'] == row['Test Name']):
            if(r['Complexity'] == 'Easy'):
                easy = easy+1;
            elif(r['Complexity'] == 'Medium'):
                medium = medium+1;
            else:
                difficult = difficult + 1;


# In[37]:


easy


# In[38]:


medium


# In[39]:


difficult



import plotly as py
import plotly.graph_objs as go

labels = ['Easy', 'Medium', 'Difficult']
values = [easy, medium, difficult]

trace = go.Pie(labels=labels, values=values)

py.plot([trace], filename='basic_pie_chart')
py.offline.show()
