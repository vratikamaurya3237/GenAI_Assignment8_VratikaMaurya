#ASSIGNMENT 8(Basic App Building): This assignment has 4 Tasks covering basic Streamlit components - titles, text input, buttons, sliders, number input, sidebar widgets, tables, metrics, and bar charts.

##Task 1: 
- Displayed a title using 'st.title("WELCOME TO  STREAMLIT!!!").
- Showed a text input box using 'st.text_input("Enteer your Name")', storing the entered value in 'name'.
- Used 'st.button("Greet Me")' inside an 'if' statement so that when the button is clicked, 'st.write(f"Hello, {name}!")' displays a greeting using the entered name.

This task made me understand that 'st.title()' displays large heading text at the top of the app, similar to a page title. 'st.text_input()' returns whatever the user has typed into the box, abd that value can be stored in a variable ('name') and reused elsewhere in the app. Wrapping code inside 'if st.button("Greet Me"):' means that code only runs when the button is actually clicked, rather than running immediately when the app loads.



##Task 2:
- Took the product price using 'st.number_input("Enter Product Proce: ")', storing it in 'price'.
- Took the discount percentage using 'st.slider("Discount Percentage", 0, 50)', storing it in 'discount', so the slider only allows values between 0 and 50.
