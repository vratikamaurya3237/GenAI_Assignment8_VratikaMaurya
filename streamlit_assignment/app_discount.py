import streamlit as st

#1. Taking product price as number input
price=st.number_input("Enter Product Price: ")

#2. Taking discount percentage as a slider from 0 to 50%
discount=st.slider("Discount Percentage", 0, 50)

#3. Calculating the discounted price on button click
if st.button("Calculate"):
    final_price=price-(price*discount/100)

    #4. Showing the result using st.success()
    st.success(f"Final Price: {final_price}")

    #Extra: Showing a comparison in a small table using st.table()
    st.table([["Before", "After"], [price, final_price]])
    