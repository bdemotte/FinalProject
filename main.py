"""
Name:           Bradley DeMotte
CS602:          Section ____
Data:           Skyscraper Data Set
URL:

Description:    This is a description of the project
"""

# Import Functions Necessary to run this program
import pandas as pd
import streamlit as st
import numpy as np
# import matplotlib.pyplot as plt


# Renaming the Columns

col_names = ['Rank',
             'Name',
             'City',
             'Address',
             'Latitude',
             'Longitude',
             'Year Completed',
             'Height',
             'In Meters',
             'In Feet',
             'Total Floors',
             'Main Material Utilized',
             'Main Function of Building',
             'Link to Website']
# Import data and read CSV into the program

skyscraperdata = pd.read_csv("Skyscrapers2021.csv", index_col=0, names=col_names, skiprows=[0])
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print(skyscraperdata)

# Create Seperator to view as I build

SEPERATOR = 500 * '='
print(SEPERATOR)
# User Input, map data, and update on the data frame for all locations



# def select_options():
#     st.sidebar.write("Filter On The Map: ")
#
# print(SEPERATOR)










# Bar chart to display number of buildings per city

# def barchart(x,y):
#     df = skyscraperdata
#     counts = ['City']
#     st.subheader("Number of Skyscrapers per City")
#     cities = sorted(df['City'].unique().tolist(), reverse=True)
#     citylist = [x for x in cities]
#     y_pos = np.arange(len(citylist))
#     plt.rcParams['figure.figsize'] = (5, 10)  # Defines run-time configuration
#     plt.bar(y_pos, counts)
#     plt.yticks(y_pos, citylist)
#     plt.title("Skyscrapers per City in the Top 100")
#     plt.xlabel('Number of Skyscrapers')
#     st.pyplot(plt)

print(SEPERATOR)







# Show various map data and information on the top 10 buildings
print(SEPERATOR)

st.title('Top 10 Skyscrapers in the World')


df = pd.read_csv("Skyscrapers2021.csv")

print("The Largest Building in the World is the Burj Khalifa\n\n")
st.header('The Largest Building in the World is the Burj Khalifa')

print("The Burj Khalifa is located at the following address:\n")
st.text('The Burj Khalifa is located at the following address: ')

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="4XZD8eEnHEVBSwaEQy4wKIVKZGfkeo5P")
location1 = geolocator.reverse((df['Latitude'][0], df['Longitude'][0]), language='en')
print(location1.address)

print(SEPERATOR)

st.header('The Second Largest Building in the World is the Shanghai Tower ')
st.text('The Shanghai Tower is located at the following address: ')
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="4XZD8eEnHEVBSwaEQy4wKIVKZGfkeo5P")
location2 = geolocator.reverse((df['Latitude'][1], df['Longitude'][1]), language='en')
print(location2.address)

print(SEPERATOR)
st.header("The Third Largest Building in the World is the Makkah Royal Clock Tower")
st.text("The Makkah Royal Clock Tower is located at the following address: ")
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="4XZD8eEnHEVBSwaEQy4wKIVKZGfkeo5P")
location3 = geolocator.reverse((df['Latitude'][2], df['Longitude'][2]), language='en')
print(location3.address)

print(SEPERATOR)
st.header("The Fourth Largest Building in the World is the Ping An Finance Center")
st.text("The Ping An Finance Center is located at the following address: ")
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="4XZD8eEnHEVBSwaEQy4wKIVKZGfkeo5P")
location4 = geolocator.reverse((df['Latitude'][3], df['Longitude'][3]), language='en')
print(location4.address)

print(SEPERATOR)
st.header("The Fifth Largest Building in theWorld is the Lotte World Tower")
st.text("The Lotte World Tower is located at the following address: ")
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="4XZD8eEnHEVBSwaEQy4wKIVKZGfkeo5P")
location5 = geolocator.reverse((df['Latitude'][4], df['Longitude'][4]), language='en')
print(location5.address)

print(SEPERATOR)
st.header("The Sixth Largest Building in the World is the One World Trade Center")
st.text("The One World Trade Center is located at the following address: ")
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="4XZD8eEnHEVBSwaEQy4wKIVKZGfkeo5P")
location6 = geolocator.reverse((df['Latitude'][5], df['Longitude'][5]), language='en')
print(location6.address)

print(SEPERATOR)
st.header("The Seventh and Eigth Tallest Building in the World are Tied! The Guangzhou CTF Finance Centre and Tianjin CTF Finance Center are both 1,739 ft tall!")
st.text("The Guangzhou CTF Finance Center is located at the following address: ")
st.text("The Tianjin CTF Finance Center is located at the following address: ")
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="4XZD8eEnHEVBSwaEQy4wKIVKZGfkeo5P")
location7 = geolocator.reverse((df['Latitude'][6], df['Longitude'][6]), language='en')
print(location7.address)

print(SEPERATOR)

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="4XZD8eEnHEVBSwaEQy4wKIVKZGfkeo5P")
location8 = geolocator.reverse((df['Latitude'][7], df['Longitude'][7]), language='en')
print(location8.address)

print(SEPERATOR)

st.header("The Ninth Largest Building in the World is the CITIC Tower")
st.text("The CITIC Tower is located at the following address: ")
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="4XZD8eEnHEVBSwaEQy4wKIVKZGfkeo5P")
location9 = geolocator.reverse((df['Latitude'][8], df['Longitude'][8]), language='en')
print(location9.address)

print(SEPERATOR)

st.header("The Tenth Largest Building in the World is the TAIPEI 101")
st.text("The TAIPEI 101 is located at the following address: ")
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="4XZD8eEnHEVBSwaEQy4wKIVKZGfkeo5P")
location10 = geolocator.reverse((df['Latitude'][9], df['Longitude'][9]), language='en')
print(location10.address)
