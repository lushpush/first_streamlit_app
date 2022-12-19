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
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.sidebar.markdown("first page")
streamlit.sidebar.markdown("second page")
streamlit.sidebar.markdown("Third page")
