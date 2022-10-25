#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


# In[69]:


data=pd.read_csv("C:/Users/Rakesh/Datasets/transformed_data.csv")
data2=pd.read_csv("C:/Users/Rakesh/Datasets/raw_data.csv")


# In[70]:


data.head()


# In[71]:


data2.head()


# In[72]:


data['COUNTRY'].value_counts()


# In[73]:


data['COUNTRY'].value_counts().mode()


# In[74]:


code=data['CODE'].unique().tolist()
country=data['COUNTRY'].unique().tolist()
hdi=[]
tc=[]
td=[]
sti=[]
population=data["POP"].unique().tolist()
gdp=[]

for i in country:
    hdi.append((data.loc[data["COUNTRY"]==i, "HDI"]).sum()/294)
    tc.append((data2.loc[data2["location"]==i, "total_cases"]).sum())
    td.append((data2.loc[data2["location"]==i, "total_deaths"]).sum())
    sti.append((data.loc[data["COUNTRY"]==i, "STI"]).sum()/294)
    population.append((data.loc[data["COUNTRY"]==i, "STI"]).sum()/294)
    
aggregated_data=pd.DataFrame(list(zip(code,country,hdi,tc,td,sti,population)),
                            columns=['Country Code','Country', 'Hdi', 'Total Cases', 'Total Deaths', 'Stringency Index', 'Population'])


# In[75]:


aggregated_data.head()


# In[76]:


data=aggregated_data.sort_values(by='Total Cases', ascending=False)
data.head()


# In[77]:


data=data.head(10)


# In[78]:


data["GDP Before Covid"] = [65279.53, 8897.49, 2100.75,11497.65, 7027.61, 9946.03,29564.74, 6001.40, 6424.98, 42354.41]
data["GDP During Covid"] = [63543.58, 6796.84, 1900.71,10126.72, 6126.87, 8346.70,27057.16, 5090.72, 5332.77, 40284.64]


# ## Analyzing the spread of covid-19

# In[79]:


figure=px.bar(data,y="Total Cases", x="Country", title="Countries with High covid cases")
figure.show()


# In[80]:


figure=px.bar(data,y="Total Deaths", x="Country", title="Countries with High covid deaths")
figure.show()


# In[81]:


fig=go.Figure()
fig.add_trace(go.Bar(
    x=data['Country'],
    y=data['Total Cases'],
    name='Total Cases',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=data['Country'],
    y=data['Total Deaths'],
    name='Total Deaths',
    marker_color='lightsalmon'
))
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()


# In[88]:


cases = data["Total Cases"].sum()
deceased = data["Total Deaths"].sum()

labels = ["Total Cases", "Total Deaths"]
values = [cases, deceased]

fig = px.pie(data, values=values, names=labels, 
             title='Percentage of Total Cases and Deaths', hole=0.5)
fig.show()


# In[82]:


death_rate=(data['Total Deaths'].sum()/data['Total Cases'].sum())*100
death_rate


# ## Stringency Index during covid 19

# In[83]:


fig=px.bar(data,x='Country',y='Total Cases',hover_data=['Population','Total Deaths'],color='Stringency Index',height=400, title='Stringency index during covid 19')
fig.show()


# In[84]:


# Analyzing covid 19 impact on Economy
fig=px.bar(data,x='Country',y='Total Cases',hover_data=['Population','Total Deaths'],color='GDP Before Covid',height=400, title='GDP Before Covid')
fig.show()


# In[85]:


# Analyzing covid 19 impact on Economy
fig=px.bar(data,x='Country',y='Total Cases',hover_data=['Population','Total Deaths'],color='GDP During Covid',height=400, title='GDP After Covid')
fig.show()


# In[86]:


fig=go.Figure()
fig.add_trace(go.Bar(
    x=data['Country'],
    y=data['GDP Before Covid'],
    name='GDP Per Capita Before Covid',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=data['Country'],
    y=data['GDP During Covid'],
    name='GDP Per capita After Covid',
    marker_color='lightsalmon'
))
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()


# In[87]:


fig=px.bar(data,x='Country',y='Total Cases', hover_data=['Population','Total Deaths'], color='Hdi', height=400, title='Human Development Index during covid 19')
fig.show()

