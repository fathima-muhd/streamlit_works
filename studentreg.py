import streamlit as st
from datetime import date

name=st.text_input("Name")
age=st.number_input("Age",min_value=0)
Dob=st.date_input("DOB",min_value=date(2000,1,1),max_value=date.today(),value=date(2006,1,1))
email=st.text_input("Email id")
gender=st.radio("Gender",["Male","Female"])
courses=st.selectbox("Courses",["Python","Dotnet","Testing"])
btn=st.button("Submit")
if btn:
    st.write("Name:",name)
    st.write("Age:",age)
    st.write("DOB:",Dob)
    st.write("Email:",email)
    st.write("Gender:",gender)
    st.write("course:",courses)
    

                          