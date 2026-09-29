import streamlit as st

st.title("MULTIPLICATION")
number1=st.number_input("Enter number1",min_value=0)
number2=st.number_input("Enter number2",min_value=0)
pro=number1*number2
btn=st.button("MUL")


if btn:
    st.write("Product is",pro)
    
