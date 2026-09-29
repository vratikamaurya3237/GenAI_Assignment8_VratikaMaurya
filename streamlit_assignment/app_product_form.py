import streamlit as st

#1. Using the sidebar to enter product details
product_name=st.sidebar.text_input("Product name")
category=st.sidebar.selectbox("Category", ["Electronics", "Clothing", "Groceries", "Books", "Toys"])
price=st.sidebar.number_input("Price")

#2. When the user clicks "Add Product"
if st.sidebar.button("Add Product"):
    #A success message
    st.success("Product added successfully!")

    #The product details in a clean format
    st.write("Product Name:", product_name)
    st.write("Category:", category)
    st.write("Price:", price)