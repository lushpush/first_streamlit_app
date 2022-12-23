import streamlit 
import pandas
import requests
import snowflake.connector

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

streamlit.header("Fruitvice fruit Advice")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT  * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_row)






fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT  * from fruit_load_list")
my_data_row = my_cur.fetchall()


fruit_choice2 = streamlit.text_input('What fruit you like to add','jackfruit')
streamlit.write('Thanks for adding ', fruit_choice2)")
streamlit.dataframe(my_data_row)





