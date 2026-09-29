import streamlit as st
from Blood import BloodAddReadRetrieveUpdateDelete
st.title("UPDATE")
id=st.number_input("ID",min_value=0)
name=st.text_input("Name")
blood_group=st.text_input("Blood Group")
phone=st.text_input("Phone")
city=st.text_input("City")
last_donation=st.date_input("Last Donation Date")
btn=st.button("UPDATE")
if btn:
    b=BloodAddReadRetrieveUpdateDelete()
    records=b.update(id,name,blood_group,phone,city,last_donation)
    if records:
        st.success("Record Updated Successfully")
    else:
        st.error("No Records Found")