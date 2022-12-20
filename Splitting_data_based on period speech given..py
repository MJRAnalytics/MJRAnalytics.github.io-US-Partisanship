# -*- coding: utf-8 -*-
"""
Splitting the data based on the time the speech was given.
"""

import pandas as pd

import scattertext as st
from datetime import datetime

df = pd.read_csv("Cleaned_data_5.csv")



columns = df.columns

texts = df["clean_text"]
party = df["Party"]
title = df["Title"]

print(party.unique())
print(len(party.unique()))

# date = df['Date_Formatted'] 

# df['Date_Formatted'] =  pd.to_datetime(df['Date_Formatted'] )

# df['Date_Formatted'] = df['Date'].dt.strftime('%m-%m-%Y')

## I need to create a dataframe of the names of each period as well as the times they encompas, so that i can use datetime objects to sort and split the data into segments to create scattertext objects with.

"""
#data retrieved from the wikipedia page section titles on wikipedia for the topic where I found the chart that gave me the idea to sort them by date to split them up. I need them smalle so the model doesn't break

First Party System,Second Party System,Third Party System,Fourth Party System,Fourth Party System,Sixth Party System,Seventh Party System


1792–1824,1828–1854,1854–1890s,1896–1932,1896–1932,1980s-2016,(2016?-present)


"""

time_periods= ["First Party System","Second Party System","Third Party System","Fourth Party System","Fifth Party System","Sixth Party System","Seventh Party System"]



dates_range = [[1792,1824],[1828,1854],[1854,1890],[1896,1932],[1932,1976],[1976,2016],[2016,2022]]

data_set = {'times': time_periods,
            'dates': dates_range}
ranges = pd.DataFrame(data_set)
# ranges = pd.DataFrame(columns={time_periods,dates_range})
# time_period_dates= datetime("1792–1824","1828–1854","1854–1890","1896–1932","1896–1932","1980s-2016","2016-2022")

# ranges =  pd.to_datetime(ranges['dates'])
# ranges = pd.date_range(ranges['dates'])


"""
Now that I have my dataframe of date ranges, I need to find a way to slice the dataframe into segments based on a range of dates
"""
# df2 = df
# df2.set_index("Date")

# dates = pd.to_datetime(df2['Date'],format="%Y-%m-%d")

# df['Year'] = df.loc[df['Date'].str[:4]]


df['Year'] = df['Date'].str[:4]


start = ranges["dates"][1][0]
start = int(start)
# df1 = df[df.columns[8]].int < start

# df1 = df.loc[df['Year'] < ranges['dates'][0][1]]

df.to_csv("Data_Year_added.csv")

end = ranges['dates'][1][1]
end = int(end)

df_clone = df
# pd.to_numeric(df_clone["Year"])

df_clone['Year'] = df_clone["Year"].astype(int)

df2 = df[df['Year'] >start]
df2 = df[(df['Year'] < end) & (df['Year'] >start)]
# df2 = df[(df['Year'] < end)]

df2.to_csv(ranges['times'][1] + ".csv")


# def split_df(start, stop):
#     indeX = 0
#     df1 = pd.DataFrame
#     for each,row in df.iterrows():
#         # print(row['Year'])
#         num = row['Year']
#         num = int(num)
#         stop = int(stop)
#         print(row['Year'])
#         print("Stop Date: "+str(end))
#         if num < end:
#             print(row['Year'])
#         break
#     # df1 = df[]
# split_df("10",ranges['dates'][0][1])

# df.loc[df['Party']=='Democratic-Republican/National Republican '
