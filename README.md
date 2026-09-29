#ASSIGNMENT 8(Basic App Building): This assignment has 4 Tasks covering basic Streamlit components - titles, text input, buttons, sliders, number input, sidebar widgets, tables, metrics, and bar charts.

##Task 1: 
- Displayed a title using 'st.title("WELCOME TO  STREAMLIT!!!").
- Showed a text input box using 'st.text_input("Enteer your Name")', storing the entered value in 'name'.
- Used 'st.button("Greet Me")' inside an 'if' statement so that when the button is clicked, 'st.write(f"Hello, {name}!")' displays a greeting using the entered name.

This task made me understand that 'st.title()' displays large heading text at the top of the app, similar to a page title. 'st.text_input()' returns whatever the user has typed into the box, abd that value can be stored in a variable ('name') and reused elsewhere in the app. Wrapping code inside 'if st.button("Greet Me"):' means that code only runs when the button is actually clicked, rather than running immediately when the app loads.



##Task 2:
- Took the product price using 'st.number_input("Enter Product Proce: ")', storing it in 'price'.
- Took the discount percentage using 'st.slider("Discount Percentage", 0, 50)', storing it in 'discount', so the slider only allows values between 0 and 50.
- Used 'if st.button("Calculate"):' so that clicking the button calculates 'final_price=price-(price*discount/100)'.
- Displayed the result using 'st.success(f"Final Price: {final_price}")', which shows the message in a green success box.
- Also, displayed a small comparison table using 'st.table([["Before"' "After"], [price, final_price]])'.

This task made me understand that 'st.slider(label, min, max)' restricts the user's input to a specific numeric range which is useful when a value like a discount percentage shouldn't go beyond certain limits. 'st.success()' is a way to visually highlight a positive/successful result to the user, different from 'st.write()'. 'st.table()' can display a simple list of lists as a small table, where each inner list becomes a row.



##Task 3:
- Used the sidebar to collect product details: 'st.sidebar.text_input("Product Name")' for the name, 'st.sidebar.selectbox("category", [...])' with five category options, and 'st.sidebar.number_input("Price")' for the price.
- Used 'if st.sidebar.button("Add Product"):' so that clicking the button in the sidebar triggers the rest of the code.
- Inside that 'if' block, displayed a success message with 'st.success("Product added successfully!")', followed by the product's details printed with three separate 'st.write()' calls.

This task made me understand that prefixing a Streamlit component with 'st.sidebar.' places that widget in the sidebar instead of the main page, which is useful for keeping input fields separate from the main content. 'st.selectbox(label, options)' lets the user pick one value from a fixed list of options, rather than typing free text. Just like the button in 'app_basic.py', the "Add Product" button's 'if' block only runs the success message and detail display after the button is actually clicked, not as soon as the sidebar loads.



##Task 4:
- Displayed a title with 'st.title("Simple Sales Dashboard")' and a short description with 'st.write("View Monthly Sales at a Glance.")'
- Created a 'months' list and used 'st.selectbox("Select a Month", months)' to let the user pick a month, storing the choice in 'selected_month'.
- Created a static dictionary 'sales' mapping each month name to a sales figure.
- Displayed the selected month's sales using 'st.metric("sales for "+selected_month, sales[selected_month])'.
- Displayed a bar chart of all the monthly sales values using 'st.bar_chart(list(sales.values()))'.

This task amde me understand that 'st.metric(labal, value)' displays a single number in a visually distinct and highlighted format, which is well suited to showing one key figure rather than a full table. 'st.bar_chart()' can plot a plain list of numbers directly, without needing pandas, since it accepts simple lists as input. Combining a 'selectbox' with a dictionary lookup is a simple way to let the user's choice control which value gets displayed elsewhere in the app.
