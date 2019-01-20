# No. of people attempts exam from start to end
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


xls = pd.ExcelFile('DataTales.xlsx')
test_scores = pd.read_excel(xls, 'Test scores')
test_master = pd.read_excel(xls, 'Test master')
test_scores.head()


# In[3]:


# .size -  find the count of each group
data = test_scores[['Test taken date']].groupby(['Test taken date']).size()


# In[4]:


datewise_exam_attems = []
for i, d in data.items():
    date = str(i).split(' ')[0]
    datewise_exam_attems.append([date, d])


data_x = [row[0] for row in datewise_exam_attems]
data_y = [row [1] for row in datewise_exam_attems]







import plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=data_x,
    y=data_y,
    name='Name of Trace 1'
)
data = [trace1]
layout = go.Layout(
    title='Number of users attempts exam',
    xaxis=dict(
        title='Dates',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='User attempts exam',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.offline.plot(fig, filename='styling-names')
