import streamlit as st
def find_highest_number(a, b, c):
    return max(a, b, c)

st.title("Highest Number Finder")
st.write("Enter three numbers and find the highest among them.")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

st.button("Find Highest")
highest = find_highest_number(num1, num2, num3)
st.success(f"The highest number among {num1}, {num2}, and {num3} is: {highest}")





    