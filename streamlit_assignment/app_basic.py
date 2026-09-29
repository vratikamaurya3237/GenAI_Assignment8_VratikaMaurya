#Importing streamlit 
import streamlit as st

#1. Displaying the Title
st.title("WELCOME TO STREAMLIT!!!")

#2. Showing a text input box for enterinf name
name=st.text_input("Enter your Name")

#3. Displaying the greeting when the "Greet Me" button is clicked
if st.button("Greet Me"):
    st.write(f"Hello, {name}!")