import streamlit as st
from Blood import BloodAddReadRetrieveUpdateDelete
st.title("RETRIEVE")
id=st.number_input("ID",min_value=0)
btn=st.button("RETRIEVE")
if btn:
    b=BloodAddReadRetrieveUpdateDelete()
    records=b.retrieve(id)
    if records:
        st.table(records)
    else:
        st.error("Not Found")