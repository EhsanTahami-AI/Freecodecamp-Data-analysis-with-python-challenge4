# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 14:32:27 2023

@author: kanoon
"""

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns


# read_file = pd.read_csv (r'C:/Users/kanoon/Desktop/freecode camp/4/fcc-forum-pageviews.txt')
# read_file.to_csv (r'C:/Users/kanoon/Desktop/freecode camp/4/fcc-forum-pageviews.csv', index=None)


df=pd.read_csv('C:/Users/kanoon/Desktop/freecode camp/4/fcc-forum-pageviews.csv')
df=df.set_index('date')


dates = df.index
x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
plt.plot(x,df['value'],'red')

plt.xlabel('Date')
plt.ylabel('Page Views')

df=df.loc[(df['value']>=df['value'].quantile(0.025))&( df['value']<=df['value'].quantile(0.975))]


df['date'] = pd.to_datetime(df.index)
df['Years']=df['date'].dt.year
df['month']=df['date'].dt.month


Groups=pd.DataFrame(df.groupby(['Years','month'], sort=False)['value'].mean().round().astype(int))



value1=Groups.values[0:8].tolist()
value2=Groups.values[8:20].tolist()
value3=Groups.values[20:32].tolist()
value4=Groups.values[32:44].tolist()


value1=[value1[i][0] for i in range(len(value1))]
value2=[value2[i][0] for i in range(len(value2))]
value3=[value3[i][0] for i in range(len(value3))]
value4=[value4[i][0] for i in range(len(value4))]


values=[value1,value2,value3,value4]

Frum_view=pd.DataFrame(values, index=['2016','2017','2018','2019'])

Frum_view.plot(kind="bar", ylim=(0,300000))



df1= pd.DataFrame({'2016':df.loc[df['Years']==2016,'value'],'2017':df.loc[df['Years']==2017,'value'],
                  '2018':df.loc[df['Years']==2018,'value'],'2019':df.loc[df['Years']==2019,'value']},
                  )


# fig,ax=plt.subplots(figsize=(16,9))  
fig, ax = plt.subplots()                      
# plt.boxplot()

sns.boxplot(df1).set_title('Year-wise Box Plot (Trend)')


month_views={}

for m in range(13):
    
    month_views[m]= df[(df['month']==m)&(df['value'])]['value']
    
df2= pd.DataFrame(month_views)
fig, ax = plt.subplots()                      
# plt.boxplot()

sns.boxplot(df2).set_title('Month-wise Box Plot (Seasonality)')
