import streamlit as st

#1. Title+Description
st.title("Simple Sales Dashboard")
st.write("View Monthly Sales at a Glance.")

#2. A selectbox with months
months=["January","February","March","April"]
selected_month=st.selectbox("Select a Month", months)

#3. A static dictionary of monthly sales
sales={"January": 1200,"February":1500,"March":900,"April":2000}

#4. Displaying the selected month's sales using st.metric()
st.metric("Sales for "+ selected_month, sales[selected_month])

#5. Displaying a bar chart using st.bar_chart()
st.bar_chart(list(sales.values()))