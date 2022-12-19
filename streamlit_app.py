import streamlit 
import pandas

streamlit.title("My Parents new healthy Diner!")
streamlit.header("Breakfast Menu")
streamlit.text ("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text ("🥗 kale, Spinach & Rocket smoothie")
streamlit.text ("🐔Hard-Boiled Free-Range Egg")
streamlit.text ("🥑🍞 Avacardo Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list  = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)