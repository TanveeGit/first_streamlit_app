# first_streamlit_app
import streamlit
streamlit.title('My Mom\'s new Healthy  Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Bluberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#multiselect fruit option
streamlit.multislect("Pick some Fruits:" , list(my_fruit_list.index))
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#display table on page
streamlit.dataframe(my_fruit_list)

