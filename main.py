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
import matplotlib.pyplot as plt


# Renaming the Columns

col_names = ['Rank',
             'Name',
             'City',
             'Address',
             'latitude',
             'longitude',
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


st.subheader('Skyscraper Data')
if st.checkbox('Show Skyscraper Data'):
    st.write(skyscraperdata)

# User Input, map data, and update on the data frame for all locations


st.title('The Worlds 100 Largest Skyscrapers Map')

def load_data(data):
  df = pd.read_csv("Skyscrapers2021.csv", index_col=0, names=col_names, skiprows=[0])
  return df

def select_options(df):
  OPTION = st.sidebar('Filter On Map')
    
  CITIES = df['City'].unique()
    
  CITIES_SELECTED = st.sidebar.multiselect('Select Cities to Display', sorted(CITIES))
        
  mark_cities = df['City'].isin(CITIES_SELECTED)
  df = df[mark_cities]
    #df_citiesselected = df[df['City'] == CITIES_SELECTED]
    
  mapping_data(df)
    
    
def mapping_data(df):
    st.map(df)
    

        
    





# barchart of heights in feet

def bar_chart(df):
  counts = []
  st.subheader("Number of Skyscrapers in each City")
  cityList =sorted(df['City'].unique().tolist())
  for i in cityList:
    counts.append(df[df['City'] == i ].shape[0])
  y_pos = np.arange(len(cityList))
  fig, ax = plt.subplots()
  ax.barh(y_pos, counts)
  ax.set_yticks(y_pos, cityList)
  ax.set_title("Skyscrapers per City")
  ax.set_xlabel('Number of Skyscrapers per City')
  st.pyplot(fig)
                 
  
def main():
  df = load_data("Skyscrapers2021.csv")
  select_options(df)
  #bar_chart(df)
  
main()                  


  
# THIS ALL WORKS DO NOT MESS WITH THIS SECTION

# Show various map data and information on the top 10 buildings


st.title('Top 10 Skyscrapers in the World')


df = pd.read_csv("Skyscrapers2021.csv")


st.header('The Largest Building in the World is the Burj Khalifa')
from PIL import Image
img1 = Image.open("burj-khalifa.jpg")

st.image(img1, width=500)

st.text('The Burj Khalifa is located at the following address: ')
st.text('Burj Khalifa, 1, Sheikh Mohammed bin Rashid Boulevard, Al Manzil, Downtown Dubai, Dubai, PO BOX 114822, United Arab Emirates')



st.header('The Second Largest Building in the World is the Shanghai Tower ')
from PIL import Image
img2 = Image.open("shanghai-tower.jpg")

st.image(img2, width=500)
st.text('The Shanghai Tower is located at the following address: ')
st.text('Dongchang Road, Lujiazui Subdistrict, Pudong, 200010, China')



st.header("The Third Largest Building in the World is the Makkah Royal Clock Tower")
from PIL import Image
img3 = Image.open("makkah-royal.jpg")

st.image(img3, width=500)
st.text("The Makkah Royal Clock Tower is located at the following address: ")
st.text('Abraj Al Bait, Western Haram Square, Al Haram, Mecca, Makkah Al Mukarramah, Makkah Region, 24231, Saudi Arabia')



st.header("The Fourth Largest Building in the World is the Ping An Finance Center")
from PIL import Image
img4 = Image.open("ping-an.jpg")

st.image(img4, width=500)
st.text("The Ping An Finance Center is located at the following address: ")
st.text('Shenzhen Convention & Exhibition Center, 111, Fuhua 3rd Road, Huanggang, Futian Sub-district, Futian District, Shenzhen, Guangdong Province, 518048, China')


st.header("The Fifth Largest Building in theWorld is the Lotte World Tower")
from PIL import Image
img5 = Image.open("lotte-tower.jpg")

st.image(img5, width=500)
st.text("The Lotte World Tower is located at the following address: ")
st.text('Lotte World Mall, 300, Olympic-ro, Bangi 2(i)-dong, Songpa-gu, Seoul, 05551, South Korea')



st.header("The Sixth Largest Building in the World is the One World Trade Center")
from PIL import Image
img6 = Image.open("shanghai-tower.jpg")

st.image(img6, width=500)
st.text("The One World Trade Center is located at the following address: ")
st.text('One World Trade Center, 285, Fulton Street, Financial District, Manhattan, New York County, New York, 10048, United States')



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



st.header("The Ninth Largest Building in the World is the CITIC Tower")
from PIL import Image
img9 = Image.open("citic-tower.jpg")

st.image(img9, width=500)
st.text("The CITIC Tower is located at the following address: ")
st.text('Workers’ Gymnasium, West Gongrentiyuchang Road, Dongcheng District, Beijing, 1000001, China')




st.header("The Tenth Largest Building in the World is the TAIPEI 101")
from PIL import Image
img10 = Image.open("taipei-tower.jpg")

st.image(img10, width=500)
st.text("The TAIPEI 101 is located at the following address: ")
st.text('Taipei 101, 7, Section 5, Xinyi Road, Xicun Village, Xinyi District, Xinyi Commercial Zone, Taipei, 11049, Taiwan')


# MAY NEED TO MAKE CHANGES HERE
  
 
  
  
  




