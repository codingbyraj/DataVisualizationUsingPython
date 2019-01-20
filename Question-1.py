
# coding: utf-8

# In[1]:


# top 10 scorer


import pandas as pd
#import matplotlib.pyplot as plt
#from matplotlib.ticker import MaxNLocator
import numpy as np
import matplotlib.pyplot as plt


# In[14]:


xls = pd.ExcelFile('DataTales.xlsx')
test_scores = pd.read_excel(xls, 'Test scores')
test_master = pd.read_excel(xls, 'Test master')


# In[15]:


test_scores.head()


# In[16]:


total_individual = test_scores.groupby(['Participant identifier'])[['Score']].sum()
# len (total_individual) # 1038
# sample = total_individual[0:10]


# In[17]:


total_individual =  total_individual.sort_values(by=['Score'],ascending=False)


# In[18]:


total_individual[0:10]


# In[19]:


total_marks = 0;
for index, row in test_master.iterrows():    
    total_marks += row['No. of questions'] * row['Marks per question']


# In[20]:


total_marks


# In[21]:


individual_percentage = []
for identifier, score in total_individual.iterrows():        
    individual_data = []
    individual_data.append(identifier)
    individual_data.append(score.values[0])
    percentage = score.values[0] / total_marks * 100
    individual_data.append(round(percentage,2))
    individual_percentage.append(individual_data)


# In[22]:


top_ten = individual_percentage[0:10]


# In[23]:


top_ten_zip = zip(*top_ten)


# In[24]:


a = list(top_ten_zip)
a[0]



names = list(a[0])
marks = list(a[1])
rank = np.arange(1,11)
columns_lables = ('User Id','Marks', 'Rank')

fig, axs =plt.subplots(2,1)
all_data = zip(names, marks, rank)
all_data = list(all_data)
final_data = [list(elem) for elem in all_data]

axs[0].axis('tight')
axs[0].axis('off')

the_table = axs[0].table(cellText=final_data,colLabels=columns_lables,loc='center')

# axs[1].plot(final_data[:,0],final_data[:,1])
plt.show()




