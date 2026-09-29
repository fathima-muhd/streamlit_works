import streamlit as st

st.title("ADDITION")
number1=st.number_input("Enter number1",min_value=0)
number2=st.number_input("Enter number2",min_value=0)
sum=number1+number2
btn=st.button("Add")


if btn:
    st.write("Sum is",sum)
    
