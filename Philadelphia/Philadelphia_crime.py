"""
This code use neighbour and crime incidents data
to find high crime neighbourhoods in philadelphia
"""

#importing libraries
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#reading neighbourhood and crime incidents datasets
neighbourhood=gpd.read_file("Data/Neighborhoods_Philadelphia")
incidents=gpd.read_file('Data/incidents_clean.shp')
#changing coordinate system of crime incidents data to epsg=2272
incidents=incidents.to_crs(epsg=2272)
#plotting the datasets together
fig, ax = plt.subplots(figsize=(20,15))
neighbourhood.plot(ax=ax, color="gray")
incidents.plot(ax=ax, markersize=0.2, color="Red")
plt.show()
#joining the two datasets togther to see in which neighboorhoods the crimes occured
neigh_incidents=gpd.sjoin(incidents, neighbourhood,how="inner", op="within")
#counting number of incidents in each neighbourhood
incident_count=neigh_incidents.groupby('NAME').size()

#conveting the Series Datatype to pandas dataframe
grouped_incidents = incident_count.to_frame().reset_index()
grouped_incidents.columns=["NAME", "Counts"]
#neighbourhoods with lowest Crime incidents
lowest_incidents=grouped_incidents[grouped_incidents['Counts']==(grouped_incidents['Counts'].min())]
#neighbourhoods with highest Crime incidents
highest_incidents=grouped_incidents[grouped_incidents['Counts']==(grouped_incidents['Counts'].max())]

print("lowest crime neighbourhood: ")
print(lowest_incidents)
print("Highest crime:")
print(highest_incidents)
#crime type in highest crime neighbour
Highest_crime=neighbourhood[neighbourhood['NAME']=="UPPER_KENSINGTON"]
#joining the two datasets togther to see crime types distribution in UPPER_KENSINGTON neighbourhood
Highest_crime_types=gpd.sjoin(incidents, Highest_crime,how="inner", op="within")
#plotting crime types in UPPER_KENSINGTON
ax=Highest_crime_types.plot(figsize=(20,15),column='text_gener',legend=True,)
ax.set_title("Crime types distribution in UPPER_KENSINGTON neighbourhood ", fontsize=16)
plt.show()

#merging the grouped incidents data with neighboorhood dataset
merged_areas=neighbourhood.merge(grouped_incidents, on="NAME", how="outer")
#plotting Crime incidents in Philadelphia
fig, ax = plt.subplots(figsize=(20,15))
merged_areas.plot(ax=ax, column='Counts',cmap='Reds', scheme='quantiles',edgecolor='grey', legend=True,  legend_kwds={'loc': 'lower right'})
ax.set_title("Crime incidents in Philadelphia", fontsize=16)
plt.show()
