
"""
This code calculates mean, maximum and minimum of Rovainemi and Helsinki temprature values in July 2017
and compare the cities summes using plots
"""
#importing libraries
import pandas as pd
import matplotlib.pyplot as plt

#reading weather csv file
Weather=pd.read_csv("data/6153237444115dat.csv",na_values=['*', '**', '***', '****', '*****', '******'])
#changing to date column date and time format
Weather['YR--MODAHRMN']=pd.to_datetime(Weather['YR--MODAHRMN'], format='%Y%m%d%H%M%S')
#creating new columns for year , month and day
Weather['year']=Weather['YR--MODAHRMN'].dt.year
Weather['month']=Weather['YR--MODAHRMN'].dt.month
Weather['day']=Weather['YR--MODAHRMN'].dt.day

#Subsetting data by colunm
selected = Weather.loc[:,['USAF','YR--MODAHRMN','TEMP','year','month','day']]
#remove rows with temprature nodata
selected.dropna(subset=['TEMP'])

#changing the data type from objects to float
selected["TEMP"] = pd.to_numeric(selected.TEMP, errors='coerce')

#changing temprature value from farhanait to Celsius
selected['TEMP_C']=round(((selected['TEMP']-32)/1.8),0)
#Subsetting base on weather station codes of Rovaniemi and Kumpula
rovaniemi = selected.loc[selected['USAF']==28450]
hel_kumpula=selected.loc[selected['USAF']==29980]

# subsetting Kumpula and Rovaniemi data for July
kumpula_july = hel_kumpula.loc[(hel_kumpula['month']==7)]
rovaniemi_july = rovaniemi.loc[(rovaniemi['month']==7)]

#aggregating daily values of mean , max, min kumpula in July
kumpula_daily_mean_july=kumpula_july.groupby(['day']).mean()
kumpula_daily_max_july=kumpula_july.groupby(['day']).max()
kumpula_daily_min_july=kumpula_july.groupby(['day']).min()

#aggregating daily values of mean , max, min rovaniemi in July
rovaniemi_daily_mean_july=rovaniemi_july.groupby(['day']).mean()
rovaniemi_daily_max_july=rovaniemi_july.groupby(['day']).max()
rovaniemi_daily_min_july=rovaniemi_july.groupby(['day']).min()

#plotting daily mean for Rovaniemi and helsinki
ax = kumpula_daily_mean_july['TEMP_C'].plot.line(figsize=(20,10),linestyle='solid',color='red',marker='o',markersize=5 ,grid=True,legend=True,label='Helsinki' )
ax = rovaniemi_daily_mean_july['TEMP_C'].plot.line(figsize=(20,10),linestyle='solid',color='blue',marker='o',markersize=5 ,grid=True,legend=True,label='Rovaniemi' )
ax.set_xlabel('Day of the month')
ax.set_ylabel('Temperature (Celsius)')
plt.title('Helsinki and Rovaniemi daily Mean temprature comparion for July 2017')
plt.show()

#plotting daily max for Rovaniemi and helsinki
ax = kumpula_daily_max_july['TEMP_C'].plot.line(figsize=(20,10),linestyle='solid',color='red',marker='o',markersize=5 ,grid=True,legend=True,label='Helsinki' )
ax = rovaniemi_daily_max_july['TEMP_C'].plot.line(figsize=(20,10),linestyle='solid',color='blue',marker='o',markersize=5 ,grid=True,legend=True,label='Rovaniemi' )
ax.set_xlabel('Day of the month')
ax.set_ylabel('Temperature (Celsius)')
plt.title('Helsinki and Rovaniemi daily Max temprature comparion for July 2017')
plt.show()

#plotting daily min for Rovaniemi and helsinki
ax = kumpula_daily_min_july['TEMP_C'].plot.line(figsize=(20,10),linestyle='solid',color='red',marker='o',markersize=5 ,grid=True,legend=True,label='Helsinki' )
ax = rovaniemi_daily_min_july['TEMP_C'].plot.line(figsize=(20,10),linestyle='solid',color='blue',marker='o',markersize=5 ,grid=True,legend=True,label='Rovaniemi' )
ax.set_xlabel('Day of the month')
ax.set_ylabel('Temperature (Celsius)')
plt.title('Helsinki and Rovaniemi daily min temprature comparion for July 2017')
plt.show()
