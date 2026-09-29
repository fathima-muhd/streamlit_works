import streamlit as st

#text_input()
name=st.text_input("Enter your name")
gender=st.text_input("Gender")


#number_input()
num1=st.number_input("Enter num1",min_value=0)
num2=st.number_input("Enter num2",min_value=0)

#Button
btn=st.button("Click")
print(btn)

if btn:
    st.write(name)
    st.write(gender)
    st.write(num1)
    st.write(num2)
        