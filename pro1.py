import streamlit as st

#title()
st.title("Welcome to my app")

#header
st.header("Main heading")

#subheader
st.subheader("Sub heading")

#write - can provide any values,dictionaries,list
st.write("My name is Fathima") 
st.write({'a':1,'b':2})
st.write(100)

#Radio button
g=st.radio('Gender',["Female","male"])
st.write(g)