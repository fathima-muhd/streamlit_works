import streamlit as st

st.title("DIVISION")
number1=st.number_input("Enter number1",min_value=0)
number2=st.number_input("Enter number2",min_value=0)
btn=st.button("DIV")

if btn:
    div=number1/number2
    st.write("Division is",div)
    
