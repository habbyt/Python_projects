"""
This code explores daily tempratures records from 1952-2017 by calculating daily means
and compare the summers of 1969,1989 and 2009 using plots
"""
#importing libraries
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

#reading weather csv file
f_name=r'data/1091402.txt'
Weather=pd.read_csv(f_name,delim_whitespace=True , skiprows=[1], na_values=[-9999] )
Weather.replace(-9999,"NaN")

#change to date column date and time format
Weather['DATE']=pd.to_datetime(Weather['DATE'], format='%Y%m%d')
#creat new columns of each month and year
Weather['year']=Weather['DATE'].dt.year
Weather['month']=Weather['DATE'].dt.month
Weather['day']=Weather['DATE'].dt.day

#calculating average temprature and change it to celcius
Weather['TEMP']=(((Weather['TMAX']+Weather['TMIN'])/2)-32)/1.8

#subset the data to only visualize avaerage temrature with time
T_data=Weather[["TEMP","day","month","year"]]
#aggregate the values by month and year to get monthly mean for each year
grp_mn_year= h_data.groupby(["month","year"], as_index=False).mean()
#organize data before plotting
Weather69y = grp_mn_year.pivot("month", "year", "TEMP")

#plotting heatmap of monthly average temprature of each years
fig, ax = plt.subplots(figsize=(12,12))
sns.heatmap(Weather69y)
plt.title('Monthly average tempratures of 1952-2017')
plt.show()
#average TMAX temperature over the Summer of 1969 (months May, June, July, and August of the year 1969)
summer69 = Weather.loc[(Weather['year']== 1969) & ((Weather['month']> 4) & (Weather['month']< 9))]
summer89 = Weather.loc[(Weather['year']== 1989) & ((Weather['month']> 4) & (Weather['month']< 9))]
summer09 = Weather.loc[(Weather['year']== 2009) & ((Weather['month']> 4) & (Weather['month']< 9))]

#aggregating daily tempratures for all summer months
summer69_grp=summer69.groupby(['month','day']).mean()
summer89_grp=summer89.groupby(['month','day']).mean()
summer09_grp=summer09.groupby(['month','day']).mean()

#Plotting temmpratures of the
ax = summer69_grp['TEMP'].plot.line(figsize=(20,15),linestyle='solid',color='red',marker='o',markersize=5 ,grid=True,legend=True,label='Summer69' )
ax = summer89_grp['TEMP'].plot.line(figsize=(20,15),linestyle='solid',color='blue',marker='o',markersize=5 ,grid=True,legend=True,label='Summer89' )
ax = summer09_grp['TEMP'].plot.line(figsize=(20,15),linestyle='solid',color='black',marker='o',markersize=5 ,grid=True,legend=True,label='Summer09' )
ax.set_xlabel('Day of the month')
ax.set_ylabel('Temperature (Celsius)')
plt.title('Daily average temprature of Summers 1969,1989 and 2009')
plt.show()
