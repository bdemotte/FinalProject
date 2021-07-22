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
#import matplotlib.pyplot as plt


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
    st.sidebar.write("Filter On Map")
    
    CITIES = df['City'].unique()
    
    CITIES_SELECTED = st.sidebar.multiselect('Select Cities to Display', sorted(CITIES))
        
    mark_cities = df['City'].isin(CITIES_SELECTED)
    df = df[mark_cities]
    #df_citiesselected = df[df['City'] == CITIES_SELECTED]
    
    mapping_data(df)
    
    
def mapping_data(df):
    st.map(df)
    

        
    
def main():
  df = load_data("Skyscrapers2021.csv")
  select_options(df)
  
main()  




# barchart of heights in feet


#st.subheader('Height of each of the Top 100 Skyscrapers')
#st.bar_chart(skyscraperdata['In Feet'])


df = pd.DataFrame({
    'building':['Burj Khalifa Dubai',
'Shanghai Tower Shanghai',
'Makkah Royal Clock Tower Mecca',
'Ping An Finance Center Shenzhen',
'Lotte World Tower Seoul',
'One World Trade Center New York City',
'Guangzhou CTF Finance Centre Guangzhou',
'Tianjin CTF Finance Centre Tianjin',
'CITIC Tower Beijing',
'TAIPEI 101 Taipei',
'Shanghai World Financial Center Shanghai',
'International Commerce Centre Hong Kong',
'Central Park Tower New York City',
'Lakhta Center St. Petersburg',
'Vincom Landmark 81 Ho Chi Minh City',
'Changsha IFS Tower T1 Changsha',
'Petronas Twin Tower 1 Kuala Lumpur',
'Petronas Twin Tower 2 Kuala Lumpur',
'Suzhou IFS Suzhou',
'Zifeng Tower Nanjing',
'The Exchange 106 Kuala Lumpur',
'Wuhan Center Tower Wuhan',
'Willis Tower Chicago',
'KK100 Shenzhen',
'Guangzhou International Finance Center Guangzhou',
'One Vanderbilt New York City',
'432 Park Avenue New York City',
'Marina 101 Dubai',
'Trump International Hotel & Tower Chicago',
'Jin Mao Tower Shanghai',
'Princess Tower Dubai',
'Al Hamra Tower Kuwait City',
'Two International Finance Centre Hong Kong',
'LCT The Sharp Landmark Tower Busan',
'Guangxi China Resources Tower Nanning',
'Guiyang International Financial Center T1 Guiyang',
'China Resources Tower Shenzhen',
'23 Marina Dubai',
'CITIC Plaza Guangzhou',
'Shum Yip Upperhills Tower 1 Shenzhen',
'30 Hudson Yards New York City',
'Shun Hing Square Shenzhen',
'Eton Place Dalian Tower 1 Dalian',
'Nanning Logan Century 1 Nanning',
'Burj Mohammed Bin Rashid Abu Dhabi',
'Empire State Building New York City',
'Elite Residence Dubai',
'Central Plaza Hong Kong',
'Federation Tower Moscow',
'Dalian International Trade Center Dalian',
'The Address Boulevard Dubai',
'Golden Eagle Tiandi Tower A Nanjing',
'Bank of China Tower Hong Kong',
'Bank of America Tower New York City',
'St. Regis Chicago Chicago',
'Almas Tower Dubai',
'Hanking Center Shenzhen',
'Gevora Hotel Dubai',
'JW Marriott Marquis Hotel Dubai Tower 1 Dubai',
'JW Marriott Marquis Hotel Dubai Tower 2 Dubai',
'Emirates Tower One Dubai',
'Raffles City Chongqing T3N Chongqing',
'Raffles City Chongqing T4N Chongqing',
'OKO - Residential Tower Moscow',
'The Torch Dubai',
'Forum 66 Tower 1 Shenyang',
'The Pinnacle Guangzhou',
'Spring City 66 Kunming',
'85 Sky Tower Kaohsiung',
'Shimao Hunan Center Changsha',
'Aon Center Chicago',
'The Center Hong Kong',
'NEVA TOWERS 2 Moscow',
'875 North Michigan Avenue Chicago',
'Four Seasons Place Kuala Lumpur',
'ADNOC Headquarters Abu Dhabi',
'One Shenzhen Bay Tower 7 Shenzhen',
'LCT The Sharp Residential Tower A Busan',
'Comcast Technology Center Philadelphia',
'Wuxi International Finance Square Wuxi',
'Heartland 66 Office Tower Wuhan',
'Chongqing World Financial Center Chongqing',
'Mercury City Tower Moscow',
'Suning Plaza Tower 1 Zhenjiang',
'Tianjin Modern City Office Tower Tianjin',
'Hengqin International Finance Center Zhuhai',
'Tianjin World Financial Center Tianjin',
'SLS Dubai Dubai',
'Wilshire Grand Center Los Angeles',
'DAMAC Heights Dubai',
'Twin Towers Guiyang, East Tower Guiyang',
'Twin Towers Guiyang, West Tower Guiyang',
'Shimao International Plaza Shanghai',
'LCT The Sharp Residential Tower B Busan',
'Rose Rayhaan by Rotana Dubai',
'Jinan Center Financial City A5-3 Jinan',
'The Address Residence - Fountain Views III Dubai',
'Minsheng Bank Building Wuhan',
'China World Tower Beijing',
'Yuexiu Fortune Center Tower 1 Wuhan'],
    'heightinfeet':['2,717 ft',
'2,073 ft',
'1,972 ft',
'1,965 ft',
'1,819 ft',
'1,776 ft',
'1,739 ft',
'1,739 ft',
'1,731 ft',
'1,667 ft',
'1,614 ft',
'1,588 ft',
'1,550 ft',
'1,516 ft',
'1,513 ft',
'1,483 ft',
'1,483 ft',
'1,483 ft',
'1,476 ft',
'1,476 ft',
'1,462 ft',
'1,454 ft',
'1,451 ft',
'1,449 ft',
'1,439 ft',
'1,401 ft',
'1,397 ft',
'1,394 ft',
'1,389 ft',
'1,380 ft',
'1,356 ft',
'1,354 ft',
'1,352 ft',
'1,350 ft',
'1,321 ft',
'1,316 ft',
'1,288 ft',
'1,287 ft',
'1,280 ft',
'1,273 ft',
'1,270 ft',
'1,260 ft',
'1,257 ft',
'1,251 ft',
'1,251 ft',
'1,250 ft',
'1,248 ft',
'1,227 ft',
'1,226 ft',
'1,214 ft',
'1,214 ft',
'1,208 ft',
'1,205 ft',
'1,200 ft',
'1,191 ft',
'1,181 ft',
'1,177 ft',
'1,169 ft',
'1,166 ft',
'1,166 ft',
'1,163 ft',
'1,163 ft',
'1,163 ft',
'1,162 ft',
'1,155 ft',
'1,150 ft',
'1,149 ft',
'1,145 ft',
'1,140 ft',
'1,138 ft',
'1,136 ft',
'1,135 ft',
'1,132 ft',
'1,128 ft',
'1,124 ft',
'1,122 ft',
'1,120 ft',
'1,113 ft',
'1,112 ft',
'1,112 ft',
'1,112 ft',
'1,112 ft',
'1,112 ft',
'1,109 ft',
'1,109 ft',
'1,108 ft',
'1,105 ft',
'1,102 ft',
'1,100 ft',
'1,099 ft',
'1,099 ft',
'1,099 ft',
'1,094 ft',
'1,093 ft',
'1,093 ft',
'1,093 ft',
'1,089 ft',
'1,086 ft',
'1,083 ft',
'1,083 ft']
})

def bar_chart(buildings, heightinfeet):
    
    building_data  = df[building_data]  # dictionary 
    

    plt.show()







  
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
  
 
  
  
  




