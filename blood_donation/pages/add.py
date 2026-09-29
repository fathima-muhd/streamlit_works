import streamlit as st
from Blood import BloodAddReadRetrieveUpdateDelete
st.title("ADD")
name=st.text_input("Name")
blood_group=st.text_input("Blood Group")
phone=st.number_input("Phone",min_value=0)
city=st.text_input("City")
last_donation=st.date_input("Last Donation Date")
btn=st.button("ADD")
if btn:
    b=BloodAddReadRetrieveUpdateDelete()
    b.add(name,blood_group,phone,city,last_donation)
    st.success("Created Successfully")