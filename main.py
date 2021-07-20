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



# Show various map data and information on the top 10 buildings
print(SEPERATOR)

st.title('Top 10 Skyscrapers in the World')


df = pd.read_csv("Skyscrapers2021.csv")

print("The Largest Building in the World is the Burj Khalifa\n\n")
st.header('The Largest Building in the World is the Burj Khalifa')
from PIL import Image
img1 = Image.open("burj-khalifa.jpg")

st.image(img1, width=500)

print("The Burj Khalifa is located at the following address:\n")
st.text('The Burj Khalifa is located at the following address: ')
st.text('Burj Khalifa, 1, Sheikh Mohammed bin Rashid Boulevard, Al Manzil, Downtown Dubai, Dubai, PO BOX 114822, United Arab Emirates')


print(SEPERATOR)

st.header('The Second Largest Building in the World is the Shanghai Tower ')
from PIL import Image
img2 = Image.open("shanghai-tower.jpg")

st.image(img2, width=500)
st.text('The Shanghai Tower is located at the following address: ')
st.text('Dongchang Road, Lujiazui Subdistrict, Pudong, 200010, China')


print(SEPERATOR)
st.header("The Third Largest Building in the World is the Makkah Royal Clock Tower")
from PIL import Image
img3 = Image.open("makkah-royal.jpg")

st.image(img3, width=500)
st.text("The Makkah Royal Clock Tower is located at the following address: ")
st.text('Abraj Al Bait, Western Haram Square, Al Haram, Mecca, Makkah Al Mukarramah, Makkah Region, 24231, Saudi Arabia')


print(SEPERATOR)
st.header("The Fourth Largest Building in the World is the Ping An Finance Center")
from PIL import Image
img4 = Image.open("ping-an.jpg")

st.image(img4, width=500)
st.text("The Ping An Finance Center is located at the following address: ")
st.text('Shenzhen Convention & Exhibition Center, 111, Fuhua 3rd Road, Huanggang, Futian Sub-district, Futian District, Shenzhen, Guangdong Province, 518048, China')

print(SEPERATOR)
st.header("The Fifth Largest Building in theWorld is the Lotte World Tower")
from PIL import Image
img5 = Image.open("lotte-tower.jpg")

st.image(img5, width=500)
st.text("The Lotte World Tower is located at the following address: ")
st.text('Lotte World Mall, 300, Olympic-ro, Bangi 2(i)-dong, Songpa-gu, Seoul, 05551, South Korea')


print(SEPERATOR)
st.header("The Sixth Largest Building in the World is the One World Trade Center")
from PIL import Image
img6 = Image.open("shanghai-tower.jpg")

st.image(img6, width=500)
st.text("The One World Trade Center is located at the following address: ")
st.text('One World Trade Center, 285, Fulton Street, Financial District, Manhattan, New York County, New York, 10048, United States')


print(SEPERATOR)
st.header("The Seventh and Eigth Tallest Building in the World are Tied! The Guangzhou CTF Finance Centre and Tianjin CTF Finance Center are both 1,739 ft tall!")
from PIL import Image
img7 = Image.open("guang-finance.jpg")

st.image(img7, width=500)
st.text("The Guangzhou CTF Finance Center is located at the following address: ")
st.text('IGC 天汇广场, 猎德西浦大街, 猎德街道, Tianhe District, Guangzhou City, Guangdong Province, 510623, China')

from PIL import Image
img8 = Image.open("tianjin-finance.jpg")
st.image(img8, width=500)
st.text("The Tianjin CTF Finance Center is located at the following address: ")
st.text('Tianjin CTF Finance Centre, 第一大街, Yujiapu Financial District, Binhai New Area, Tianjin, 300457, China')

print(SEPERATOR)

st.header("The Ninth Largest Building in the World is the CITIC Tower")
from PIL import Image
img9 = Image.open("citic-tower.jpg")

st.image(img9, width=500)
st.text("The CITIC Tower is located at the following address: ")
st.text('Workers’ Gymnasium, West Gongrentiyuchang Road, Dongcheng District, Beijing, 1000001, China')


print(SEPERATOR)

st.header("The Tenth Largest Building in the World is the TAIPEI 101")
from PIL import Image
img10 = Image.open("taipei-tower.jpg")

st.image(img10, width=500)
st.text("The TAIPEI 101 is located at the following address: ")
st.text('Taipei 101, 7, Section 5, Xinyi Road, Xicun Village, Xinyi District, Xinyi Commercial Zone, Taipei, 11049, Taiwan')


st.title('Where they are located: ')



data = pd.DataFrame({
  'top ten': ['Burj Khalifa', 'Shanghai Tower', 'Makkah Royal Clock Tower', 'Ping An Finance Center', 'Lotte World Tower', 'One World Trade Center', 'Guangzhou CTF Finance Centre', 'Tianjin CTF Finance Centre', 'CITIC Tower', 'TAIPEI 101'],
  'lat' : [25.197197, 31.233518, 21.4186828, 22.533096, 37.5124705, 40.7127431, 23.1175997, 39.021667, 39.930818, 25.0336752],
  'lon' : [55.2743764, 121.505618, 39.8252756, 114.055865, 127.1023832, -74.0133795, 113.3259267, 117.698056, 116.4359296, 121.5648831]
})

if st.checkbox('Per Location'):
    st.subheader('Building Name')
    st.write(data)
st.map(data)


