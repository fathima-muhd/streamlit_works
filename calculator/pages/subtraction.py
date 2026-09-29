import streamlit as st

st.title("SUBTRACTION")
number1=st.number_input("Enter number1",min_value=0)
number2=st.number_input("Enter number2",min_value=0)
diff=number1-number2
btn=st.button("SUB")

if btn:
    st.write("Difference is",diff)
    
