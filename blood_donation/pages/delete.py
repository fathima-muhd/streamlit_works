import streamlit as st
from Blood import BloodAddReadRetrieveUpdateDelete
st.title("DELETE")
id=st.number_input("ID",min_value=0)
btn=st.button("DELETE")
if btn:
    b=BloodAddReadRetrieveUpdateDelete()
    records=b.delete(id)
    if records:
        st.success("Record Deleted Successfully")
    else:
        st.error("No Records Found")